from . import chroma_client
import os
import logging
from langchain_openai import AzureChatOpenAI
from langgraph.graph import MessagesState, StateGraph
from typing import Union, Literal
from langchain.prompts import PromptTemplate
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langgraph.graph import END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://eu.api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "4omini_Version"

os.environ["TOKENIZERS_PARALLELISM"] = "false"

os.environ["AZURE_OPENAI_API_KEY"]= os.getenv("AZURE_OPENAI_KEY") 
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2024-08-01-preview"

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini",
    model="gpt-4o-mini",
    max_retries=2,
    temperature=0.1,
    max_tokens=800,
    timeout=None,
)


logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    handlers=[
        logging.StreamHandler(),  
        logging.FileHandler("app.log", mode="w")  
    ]
)
logger = logging.getLogger(__name__)

# Define a simple classifier prompt
classifier_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    You are a legal assistant. Analyze the user query and decide which category it belongs to:
    - Legal Cases
    - Laws

    User Query: "{query}"
    You have only these two options to choose from:
    either output "Legal Cases" if it's more relevant to legal cases, or "Laws" if it's more related to laws.
    """
)

# Function to classify query
def classify_query(query: str) -> str:
    logger.info("============================ Starting query classification for: %s", query)
    chain = classifier_prompt | llm
    result = chain.invoke(query) 
    logger.info("============================ Query classified as: %s", result.content if hasattr(result, 'content') else "Error Warning")
    return result.content


graph_builder = StateGraph(MessagesState)

@tool(response_format="content_and_artifact")
def retrieve(query: str):
    """
    Retrieve information related to a query.

    This function fetches relevant documents based on the provided query.
    It uses a vector store to perform similarity search and returns 
    both a serialized string of the documents and their raw format.
    """

    classification = classify_query(query)
    n = 21
    # Define retrieval proportions
    if classification == "Legal Cases":
        n_cases = int(n * 0.7)  # 70% from cases, 30% from laws
        n_laws = n - n_cases
        
    elif classification == "Laws":
        n_laws = int(n * 0.7)  # 70% from laws, 30% from cases
        n_cases = n - n_laws
    else:
        # Default to a 50-50 split if uncertain
        n_cases = n // 2
        n_laws = n - n_cases
    # Retrieve documents
    docs_cases = chroma_client.case_vectorstore.similarity_search(query, n_cases)
    docs_laws = chroma_client.law_vectorstore.similarity_search(query, n_laws)

    # Combine results
    combined_docs = docs_cases + docs_laws
    
    serialized = "\n\n".join(
        f"Document {idx + 1}:\n"
        f"Source: {doc.metadata}\n"
        f"Content:\n{doc.page_content.strip()}\n"
        f"{'-' * 50}"
        for idx, doc in enumerate(combined_docs)
    )
    # logger.info("Combined Documents:\n%s", serialized)
    return serialized, combined_docs

def tools_condition(state: MessagesState) -> Union[str, Literal["END"]]:
    """Decide whether to use the tool or end it, based on the last AI message."""
    last_message = state["messages"][-1]
    
    # If the message is not an AI message, end
    if last_message.type != "ai":
        return END
        
    # If the message contains a tool call, route to the tool
    if last_message.tool_calls:
        return "tools"
        
    # Otherwise, end
    return END



# Step1: Generate an AIMessage that may include a tool-call to be sent. AIMessages are final response.
def query_or_respond(state: MessagesState):
    """Generate tool call for retrieval or respond."""
    llm_with_tools = llm.bind_tools([retrieve])
    response = llm_with_tools.invoke(state["messages"])
    # MessagesState appends messages to state instead of overwriting
    return {"messages": [response]}


# Step2: Execute the retrieval.
tools = ToolNode([retrieve])


# Step 3: Generate a response using the retrieved content. The retrieved documents are ToolMessage
def generate(state: MessagesState):
    """Generate answer."""
    # Get generated ToolMessages
    recent_tool_messages = []
    for message in reversed(state["messages"]):
        if message.type == "tool":
            recent_tool_messages.append(message)
        else:
            break
    tool_messages = recent_tool_messages[::-1]

    # Format into prompt
    docs_content = "\n\n".join(doc.content for doc in tool_messages)
    system_message_content = (
        "You must retrieve documents according to the classification and use them as context to answer the question."
        "If you don’t have enough context from these documents, answer based on your general knowledge." 
        "Keep the answer as concise as possible."
        "\n\n"
        f"{docs_content}"
    )
    conversation_messages = [
        message
        for message in state["messages"]
        if message.type in ("human", "system")
        or (message.type == "ai" and not message.tool_calls)
    ]
    prompt = [SystemMessage(system_message_content)] + conversation_messages

    # Run
    response = llm.invoke(prompt)
    return {"messages": [response]}



# Build graph
graph_builder = StateGraph(MessagesState)

graph_builder.add_node(query_or_respond)
graph_builder.add_node(tools)
graph_builder.add_node(generate)

graph_builder.set_entry_point("query_or_respond")
graph_builder.add_conditional_edges(
    "query_or_respond",
    tools_condition,
    {END: END, "tools": "tools"},
)
graph_builder.add_edge("tools", "generate")
graph_builder.add_edge("generate", END)

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)


config = {"configurable": {"thread_id": "abc123"}}



initial_system_message = SystemMessage(
    "You are a legal assistant."
    "For any legal question, you should first use the retrieve tool to obtain the relevant information before providing an answer."
    "Use your general knowledge as a supplement only when the information retrieved is insufficient."
)

def run_query(query):
    for step in graph.stream(
        {"messages": [
            initial_system_message,
            {"role": "user", "content": query}
        ]},
        stream_mode="values",
        config=config,
    ): 
        step["messages"][-1].pretty_print()

        if "tool_calls" in step["messages"][-1].additional_kwargs:
            print("********** TOOL CALL DETECTED **********")
    
    return step["messages"][-1].content



if __name__ == "__main__":
    # input_message = "German regulations on the date on which a renter may withdraw from a property"
    # input_message = "Give me cases about conflict between the landlord and the tenant about the date of moving out of the house"
    input_message = "Was macht einen rechtlich gültigen Mietvertrag aus?"
    # input_message = "What should I do if my neighbour keeps using vaccum cleaner on Sunday"
    s = run_query(input_message)
    s = classify_query(input_message)


# # input_message = "Give me cases about stealing or robbing jewellery stores"
# # s = run_query(input_message)
# # # # print("============================ Answer on UI:", s)


# # input_message = "I would like to know about the second case that you've mentioned."
# # s = run_query(input_message)
# # print("###########", s)

# # # input_message = "Which case is the worst?"
# # # s = run_query(input_message)
# # # # print("###########", s)

# # # input_message = "Repeat your last question"
