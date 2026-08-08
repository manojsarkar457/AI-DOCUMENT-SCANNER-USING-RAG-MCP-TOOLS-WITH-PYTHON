"""
utils/vectorstore.py
Create, Save, Load and Search FAISS Vector Database
"""

import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

VECTOR_DB = "vectordb"

# Embeddings
def get_embeddings(provider = "OpenAI"):
    if provider == "Gemini":
        return GoogleGenerativeAIEmbeddings(
            model = "models/embedding-001"
        )
    else:
        return OpenAIEmbeddings(
            model = "text-embedding-3-small"
        )

# Create Vector Store
def create_vectorstore(documents, provider = "OpenAI"):
    """
    Create FAISS Vector Store.
    """

    embeddings = get_embeddings(provider)
    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )
    return vectorstore

# Save Vector Store
def save_vectorstore(vectorstore, folder_path = VECTOR_DB):
    """
    Save Vector Store.
    """
    os.makedirs(folder_path, exist_ok=True)
    vectorstore.save_local(folder_path)

# Load Vector Store
def load_vectorstore(
        provider = "OpenAI",
        folder_path = VECTOR_DB
):
    """
    Load existing Vector Store.
    """

    embeddings = get_embeddings(provider)
    return FAISS.load_local(
        folder_path=folder_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )
# Similarity Search
def similarity_search(vectorstore, query, k=4):
    """
    Retrieve relevant chunks.
    """

    return vectorstore.similarity_search(query=query, k=k)

# MMR Search
def mmr_search(vectorstore, query, k=4, fetch_k=20):
    """
    Max Marginal Relevance Search.
    """

    return vectorstore.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=fetch_k
    )

# Check Existing Vector DB
def vectorstore_exists(folder_path=VECTOR_DB):
    return (
        os.path.exists(os.path.join(folder_path, "index.faiss"))
        and
        os.path.exists(os.path.join(folder_path, "index.pkl"))
    )