import streamlit as st

from utils.file_manager import save_upload_files
from utils.chat_history import add_messages, display_chat
from mcp_tools.excel_tool import process_excel, ask_excel

def excel_assistant(model):
    st.header("📊 Excel  Assistant")
    uploaded_files = st.file_uploader("Upload Excel Files", type=["xlsx", "xls"], accept_multiple_files=True, key="excel_uploader")

    if uploaded_files:
        if st.button("📚 Process Excel Files", use_container_width=True):
            with st.spinner("Processing Excel Files...."):
                file_paths = save_upload_files(uploaded_files)

                message = process_excel(file_paths=file_paths, provider=model)
            st.success(message)
    #st.divider()
    display_chat()

    question = st.chat_input("Ask anything about your Excel files.....")
    if question:
        add_messages("user", question)
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking....."):
                answer = ask_excel(question=question, provider=model)
                st.markdown(answer)

            add_messages("assistant", answer)