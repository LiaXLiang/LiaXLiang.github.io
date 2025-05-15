import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

client = chromadb.HttpClient(
    host="localhost",
    port=9000
)

# Initialize the embedding model and Chroma vector store
embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large-instruct")

case_vectorstore = Chroma(
    client=client,
    collection_name="cases_database",
    embedding_function=embeddings
)

law_vectorstore = Chroma(
    client=client,
    collection_name="laws_database_2",
    embedding_function=embeddings
)

# Test whether collections are available
# collections = client.list_collections()
# print("Collections available in the Chroma database:")
# for collection in collections:
#     print(f"- {collection.name}")


case_retriever = case_vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
law_retriever = law_vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

## Test the database retrieval
# user_query = ("Laws about deliberate arson.")
# retrieved_docs = law_retriever.invoke(user_query)
# for i, doc in enumerate(retrieved_docs):
#     print(f"Document {i+1}:\n", doc.page_content)
#     print("="*80)