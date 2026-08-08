"""
Split LangChain Documents into smaller chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=500, chunk_overlap=200):
    """
    Split documents into smaller chunks.
    Args:
        documents (list): LangChain Documents
        chunk_size (int): Chunk size
        chunk_overlap (int): Overlap between chunks
    Returns:
        list: Split documents
    """

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    return splitter.split_documents(documents)