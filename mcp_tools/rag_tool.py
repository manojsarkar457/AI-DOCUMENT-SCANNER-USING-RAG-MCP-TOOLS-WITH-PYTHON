from utils.loaders import load_documents
from utils.splitter import split_documents
from utils.vectorstore import (create_vectorstore, save_vectorstore, load_vectorstore, similarity_search, vectorstore_exists)

def build_vector_database(file_paths, provider="OpenAI"):
    documents = load_documents(file_paths)
    chunks = split_documents(documents)
    vectorstore = create_vectorstore(documents=chunks, provider=provider)

    save_vectorstore(vectorstore)
    return len(chunks)

def search_documents(question, provider="OpenAI", k=4):
    if not vectorstore_exists():
        return []

    vectorstore = load_vectorstore(provider)
    return similarity_search(vectorstore, question, k)

def get_context(question, provider="OpenAI", k=4):
    docs = search_documents(question, provider, k)
    if not docs:
        return ""
    context = ""
    for doc in docs:
        context += doc.page_content
        context += "\n\n"
    return context

def get_sources(question, provider="OpenAI", k=4):
    docs = search_documents(question, provider, k)

    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown")
        if source not in sources:
            sources.append(source)
    return sources