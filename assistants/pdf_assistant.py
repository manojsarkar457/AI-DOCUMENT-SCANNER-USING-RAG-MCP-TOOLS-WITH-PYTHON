import streamlit as st

from utils.file_manager import save_upload_files
from utils.chat_history import (add_messages, display_chat)

from mcp_tools.pdf_tool import (process_pdf, ask_pdf)

def pdf_assistant(model):
    st.header("📄 PDF Assistant")
    uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        if st.button("📚 Process PDFs", use_container_width=True):
            with st.spinner("Processing PDFs...."):
                file_paths = save_upload_files(uploaded_files)

                message = process_pdf(file_paths=file_paths, provider=model)
            st.success(message)
    #st.divider()
    display_chat()

    question = st.chat_input("Ask anything about your PDF...")
    if question:
        add_messages("user", question)
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking....."):
                answer = ask_pdf(question=question, provider=model)
                st.markdown(answer)

            add_messages("assistant", answer)