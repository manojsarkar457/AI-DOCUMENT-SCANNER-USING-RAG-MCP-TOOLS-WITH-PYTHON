import streamlit as st

from utils.file_manager import save_upload_files
from utils.chat_history import (add_messages, display_chat)

from mcp_tools.csv_tool import (process_csv, ask_csv)

def csv_assistant(model):
    st.header("📑 CSV Assistant")
    uploaded_files = st.file_uploader("Upload CSV Files", type=["csv"], accept_multiple_files=True, key="csv_uploader")

    if uploaded_files:
        if st.button("📚 Process CSV Files", use_container_width=True):
            with st.spinner("Processing CSV Files...."):
                file_paths = save_upload_files(uploaded_files)

                message = process_csv(file_paths=file_paths, provider=model)
            st.success(message)
    #st.divider()
    display_chat()

    question = st.chat_input("Ask anything about your CSV files.....")
    if question:
        add_messages("user", question)
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking....."):
                answer = ask_csv(question=question, provider=model)
                st.markdown(answer)

            add_messages("assistant", answer)