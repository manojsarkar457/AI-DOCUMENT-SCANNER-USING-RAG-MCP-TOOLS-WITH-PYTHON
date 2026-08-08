from mcp.server.fastmcp import FastMCP

from mcp_tools.pdf_tool import (process_pdf, ask_pdf)
from mcp_tools.excel_tool import (process_excel, ask_excel)
from mcp_tools.csv_tool import (process_csv, ask_csv)
from mcp_tools.docx_tool import (process_docx, ask_docx)

# Create MCP Server
mcp = FastMCP("AI Document Assistant")

# PDF
@mcp.tool()
def upload_pdf(file_paths: list[str], provider: str = "OpenAI"):
    return process_pdf(file_paths=file_paths, provider=provider)

@mcp.tool()
def search_pdf(question: str, provider: str = "OpenAI"):
    return ask_pdf(question=question, provider=provider)

# Excel
@mcp.tool()
def upload_excel(file_paths: list[str], provider: str = "OpenAI"):
    return process_excel(file_paths=file_paths, provider=provider)

@mcp.tool()
def search_excel(question: str, provider: str = "OpenAI"):
    return ask_excel(question=question, provider=provider)

# CSV
@mcp.tool()
def upload_csv(file_paths: list[str], provider: str = "OpenAI"):
    return process_csv(file_paths=file_paths, provider=provider)

@mcp.tool()
def search_csv(question: str, provider: str = "OpenAI"):
    return ask_csv(question=question, provider=provider)

# DOCX
@mcp.tool()
def upload_docx(file_paths: list[str], provider: str = "OpenAI"):
    return process_docx(file_paths=file_paths, provider=provider)

@mcp.tool()
def search_docx(question: str, provider: str = "OpenAI"):
    return ask_docx(question=question, provider=provider)

# Universal Search
@mcp.tool()
def search_documents(
    assistant: str,
    question: str,
    provider: str = "OpenAI"
):
    assistant = assistant.lower()

    if assistant == "pdf":
        return ask_pdf(question, provider)

    elif assistant == "excel":
        return ask_excel(question, provider)

    elif assistant == "csv":
        return ask_csv(question, provider)

    elif assistant == "docx":
        return ask_docx(question, provider)

    return "Unsupported Assistant"

# Run Server
if __name__ == "__main__":
    mcp.run()