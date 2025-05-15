import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain import hub


# Specify the directory and collection name
script_dir = os.path.dirname(os.path.abspath(__file__))
persist_directory = os.path.join(script_dir, "./anzeigeistraus/cases_storage_0")
collection_name = "cases_storage_0"

# Initialize the embedding model and Chroma vector store
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(
    persist_directory=persist_directory,
    collection_name=collection_name,
    embedding_function=embedding
)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})

# I. Test using Retriever
# user_query = ("Cases about jeans")
# retrieved_docs = retriever.invoke(user_query)



# II. Test using Till's testing.py
# query = "Cases about jeans"  # Broad query term to test retrieval
# retrieved_docs = vectorstore.similarity_search(query, k=5)  # Retrieve top 5 documents




# Anyway this must be uncommented if you wanna test it
# Print the results to verify content
# for i, doc in enumerate(retrieved_docs):
#     print(f"Document {i+1}:\n", doc.page_content)
#     print("="*80)