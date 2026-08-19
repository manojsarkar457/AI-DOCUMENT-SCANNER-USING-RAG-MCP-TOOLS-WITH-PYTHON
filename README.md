# 🤖 AI Document Scanner Using RAG & MCP Tools with Python

An intelligent **AI Document Scanner and Assistant** built with Python that allows users to upload documents, search their contents, and ask questions using **Retrieval-Augmented Generation (RAG)** and **Model Context Protocol (MCP)** tools.

The application combines document processing, text chunking, vector embeddings, FAISS similarity search, MCP tools, and Large Language Models (LLMs) to provide contextual answers from uploaded documents.

---

## 📌 Project Overview

Traditional document search often depends on exact keyword matching. This project uses **semantic search** through vector embeddings, allowing users to ask questions naturally.

The system:

1. Accepts documents from the user.
2. Extracts text from the documents.
3. Splits the text into smaller chunks.
4. Converts chunks into vector embeddings.
5. Stores embeddings in a FAISS vector database.
6. Retrieves relevant chunks when the user asks a question.
7. Uses an LLM to generate an answer based on the retrieved context.
8. Uses MCP tools to expose document search and analysis capabilities to an AI agent.

---

## ✨ Features

* 📄 PDF document processing
* 📊 CSV and Excel data analysis
* 🔍 Semantic document search
* 🧠 Retrieval-Augmented Generation (RAG)
* 🗂️ FAISS vector database
* 🤖 LLM-powered question answering
* 🔌 Model Context Protocol (MCP) tool integration
* 💬 Interactive document chat
* 🌐 Streamlit web interface
* 📑 Document chunking and embeddings
* 🔎 Context-aware information retrieval
* 🧩 Modular project architecture
* 🔐 Environment-variable based API key configuration

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Document Loader   │
                    │  PDF / CSV / Excel  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Text Splitting &    │
                    │   Preprocessing     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Embedding Model   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  FAISS Vector Store │
                    └──────────┬──────────┘
                               │
                         User Question
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Semantic Retrieval  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     MCP Tools       │
                    │ PDF / CSV / Excel   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    RAG Pipeline     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        LLM          │
                    │ Gemini / Other LLM  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     AI Response     │
                    └─────────────────────┘
```

---

## 🔄 RAG Workflow

### 1. Document Loading

Documents are loaded using appropriate Python libraries.

* PDF → `PyPDF`
* Excel → `Pandas` / `OpenPyXL`
* CSV → `Pandas`

### 2. Text Splitting

Large documents are divided into smaller chunks using a text splitter. This improves retrieval accuracy and keeps prompts manageable.

### 3. Embeddings

Each text chunk is converted into a numerical vector representing its semantic meaning.

```text
Document Text
      |
      v
Embedding Model
      |
      v
Numerical Vector
```

### 4. Vector Storage

The generated vectors are stored in **FAISS**, enabling efficient similarity-based retrieval.

### 5. Semantic Search

When the user asks a question, the question is converted into an embedding and compared against stored document vectors. The most relevant chunks are retrieved.

### 6. Response Generation

The retrieved context is passed to the LLM along with the user's question. The model generates an answer based on the retrieved information.

---

## 🔌 MCP Integration

The project uses **Model Context Protocol (MCP)** to expose document-related functionality as tools that an AI agent can call.

### Example MCP Tools

```text
search_pdf(question)
find_employee(name)
analyze_csv(question)
```

This allows an AI system to retrieve information from documents or analyze structured data when required.

### Example MCP Workflow

```text
User
  |
  v
"Find the details of Manoj Sarkar."
  |
  v
AI Agent
  |
  v
MCP Tool
find_employee("Manoj Sarkar")
  |
  v
Vector / Document Search
  |
  v
Relevant Information
  |
  v
LLM
  |
  v
Final Answer
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Core programming language       |
| Streamlit         | Web application interface       |
| LangChain         | RAG and document processing     |
| FAISS             | Vector similarity search        |
| MCP               | AI tool integration             |
| Google Gemini     | Large Language Model            |
| PyPDF             | PDF text extraction             |
| Pandas            | Data processing                 |
| OpenPyXL          | Excel file processing           |
| Vector Embeddings | Semantic representation         |
| python-dotenv     | Environment variable management |

---

## 📁 Project Structure

```text
AI-Document-Scanner/
│
├── app.py
├── server.py
├── client.py
├── requirements.txt
├── README.md
│
├── assistants/
│   ├── pdf_assistant.py
│   ├── excel_assistant.py
│   ├── csv_assistant.py
│   └── docx_assistant.py
│
├── utils/
│   ├── loaders.py
│   ├── splitter.py
│   ├── vectorstore.py
│   ├── rag_pipeline.py
│   ├── llm_provider.py
│   └── prompts.py
│
├── mcp_tools/
│   ├── pdf_tool.py
│   ├── rag_tool.py
│   ├── excel_tool.py
│   └── csv_tool.py
│
├── data/
│   └── sample_documents/
│
└── .env
```

> The exact files and folders may vary depending on the current implementation.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Document-Scanner.git
cd AI-Document-Scanner
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

### Google Gemini

```env
GOOGLE_API_KEY=your_google_api_key
```

If your implementation also supports OpenAI:

```env
OPENAI_API_KEY=your_openai_api_key
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
.faiss/
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the application in your browser:

```text
http://localhost:8501
```

---

## 💡 Example Questions

After uploading a document, users can ask questions such as:

```text
What is this document about?
```

```text
Summarize the document.
```

```text
Who is Manoj Sarkar?
```

```text
Find the employee with the highest sales.
```

```text
What is the total revenue?
```

```text
What are the main points discussed in the document?
```

```text
Find information related to a specific topic.
```

---

## 🧪 Example RAG Pipeline

```python
documents = load_documents(file_path)

chunks = split_documents(documents)

vectorstore = create_vectorstore(chunks)

results = vectorstore.similarity_search(query, k=4)

context = "\n".join(
    document.page_content
    for document in results
)

response = llm.invoke(
    f"""
    Answer the question using the following context:

    {context}

    Question:
    {query}
    """
)
```

---

## 🔌 Example MCP Tool

A simplified MCP tool can look like:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Document Assistant")


@mcp.tool()
def search_pdf(question: str) -> str:
    """Search the uploaded PDF and return relevant information."""

    # Vector search implementation
    return "Relevant document information"
```

The MCP server exposes this functionality so that an AI client or agent can use it when required.

---

## 🎯 Use Cases

This project can be useful for:

* 📚 Research document assistants
* 🏢 Company knowledge bases
* 📄 Legal document search
* 🎓 Educational document analysis
* 👨‍💼 HR document assistants
* 📊 Business report analysis
* 🧾 Invoice and report processing
* 📑 Policy and documentation search
* 🤖 AI-powered knowledge management systems

---

## 🚀 Future Enhancements

* [ ] Multi-document conversational memory
* [ ] DOCX support
* [ ] Image document scanning
* [ ] OCR integration
* [ ] Voice input
* [ ] Source/page citations
* [ ] Chat history
* [ ] User authentication
* [ ] Multi-user support
* [ ] Cloud deployment
* [ ] Advanced agentic workflows
* [ ] Additional MCP tools
* [ ] Database integration
* [ ] Document summarization
* [ ] Hybrid keyword + semantic search
* [ ] Reranking for improved retrieval accuracy

---

## 🔐 Security

For security:

* Store API keys in `.env`.
* Never upload API keys to GitHub.
* Add `.env` to `.gitignore`.
* Avoid storing sensitive documents in public repositories.
* Validate uploaded files before processing.

---

## 🧠 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

* Python
* Generative AI
* Large Language Models
* Retrieval-Augmented Generation
* Vector Databases
* Semantic Search
* Embeddings
* LangChain
* FAISS
* Model Context Protocol
* AI Agents
* Streamlit
* Document Processing
* API Integration

---

## 👨‍💻 Author

**Manoj Sarkar**

B.Tech in Computer Science & Engineering

Interested in **Python, Generative AI, Agentic AI, RAG, MCP, and AI-powered applications**.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---
