import pandas as pd
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, UnstructuredWordDocumentLoader

# PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

# CSV
def load_csv(file_path):
    loader = CSVLoader(file_path)
    return loader.load()

# DOCX
def load_docx(file_path):
    loader = UnstructuredWordDocumentLoader(file_path)
    return loader.load()

# Excel
def load_excel(file_path):
    documents = []
    sheets = pd.read_excel(file_path, sheet_name=None)

    for sheet_name, dataframe in sheets.items():
        dataframe = dataframe.fillna("")
        for index, row in dataframe.iterrows():
            content = "\n".join(
                [
                    f"{column}:{row[column]}"
                    for column in dataframe.columns
                ]
            )
            documents.append(
                Document(
                    page_content=content,
                    metadata = {
                        "source" :file_path,
                        "sheet" : sheet_name,
                        "row" : index + 1,
                    },
                )
            )
    return documents

# Universal Loader
def load_documents(file_paths):
    Documents = []

    for file_path in file_paths:
        extension = file_path.split(".")[-1].lower()
        if extension == "pdf":
            Documents.extend(load_pdf(file_path))

        elif extension == "csv":
            Documents.extend(load_csv(file_path))

        elif extension in ["xlsx", "xls"]:
            Documents.extend(load_excel(file_path))

        elif extension == "docx":
            Documents.extend(load_docx(file_path))
    return Documents