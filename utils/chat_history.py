import streamlit as st

# Initialize
def initialize_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

# Add Message
def add_messages(role, content):
    st.session_state.messages.append({
        "role" : role,
        "content" : content
    })

# Get Chat History
def get_chat_history():
    return st.session_state.messages

#Recent Chat
def get_recent_chat(limit=5):
    return st.session_state.messages[-limit:]

# Clear Chat
def clear_chat():
    st.session_state.messages = []

# Download Chat
def download_chat():
    chat = ""

    for message in st.session_state.messages:
        role = message["role"].upper()
        chat += f"{role}\n"
        chat += f"{message['content']}"
    return chat

# Dsiplay Chat
def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Build Conversation History
def conversation_history():
    history = ""
    for message in st.session_state.messages:
        history += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )
    return history