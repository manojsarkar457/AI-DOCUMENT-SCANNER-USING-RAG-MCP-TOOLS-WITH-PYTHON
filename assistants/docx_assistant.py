import streamlit as st

from utils.file_manager import save_upload_files
from utils.chat_history import (add_messages, display_chat)

from mcp_tools.docx_tool import (process_docx, ask_docx)

def docx_assistant(model):
    st.header("📝 DOCX  Assistant")
    uploaded_files = st.file_uploader("Upload DOCX Files", type=["docx"], accept_multiple_files=True, key="docx_uploader")

    if uploaded_files:
        if st.button("📚 Process DOCX Files", use_container_width=True):
            with st.spinner("Processing DOCX Files...."):
                file_paths = save_upload_files(uploaded_files)

                message = process_docx(file_paths=file_paths, provider=model)
            st.success(message)
    #st.divider()
    display_chat()

    question = st.chat_input("Ask anything about your DOCX files.....")
    if question:
        add_messages("user", question)
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking....."):
                answer = ask_docx(question=question, provider=model)
                st.markdown(answer)

            add_messages("assistant", answer)