import streamlit as st

# Import Assistants
from assistants.pdf_assistant import pdf_assistant
from assistants.excel_assistant import excel_assistant
from assistants.csv_assistant import csv_assistant
from assistants.docx_assistant import docx_assistant

# Page Configuration
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("🤖 AI Document Assistant")
st.caption("Chat with PDF, Excel, CSV, & DOCX files using OpenAI or Gemini")

# Sidebar
with st.sidebar:
    st.header("⚙ Settings")

    # AI Model
    model = st.selectbox(
        "Choose AI Model",
        [
            "OpenAI",
            "Gemini"
        ]
    )

    st.divider()

    # Assistant Selection
    assistant = st.selectbox(
        "Choose Assistant",
        [
            "PDF Assistant",
            "Excel Assistant",
            "CSV Assistant",
            "DOCX Assistant"
        ]
    )

    st.divider()

    st.subheader("💬 Recent Chat")

    if st.session_state.messages:
        recent = st.session_state.messages[-5:]
        for msg in recent:
            icon = "🧑" if msg["role"] == "user" else "🤖"
            st.caption(f"{icon} {msg['content'][:50]}...")
    else:
        st.caption("No recent chats.")

    st.divider()

    chat_text = ""
    for msg in st.session_state.messages:
        chat_text += f"{msg['role'].upper()}:\n{msg['content']}\n\n"

    st.download_button(
        "⬇ Download Chat",
        data = chat_text,
        file_name = "chat_history.txt",
        mime = 'text/plain',
        use_container_width = True
    )
    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

# Assistant Routing
if assistant == "PDF Assistant":
    pdf_assistant(model)

elif assistant == "Excel Assistant":
     excel_assistant(model)

elif assistant == "CSV Assistant":
    csv_assistant(model)

elif assistant == "DOCX Assistant":
    docx_assistant(model)

st.divider()

st.markdown(
    """
        <div style='text-align:center; color:gray; font-size:14px; padding:10px'>
        Developed & Maintained by <b>Manoj Sarkar</b>
        </div>
    """,
    unsafe_allow_html=True
)