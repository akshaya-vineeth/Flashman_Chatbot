import streamlit as st
from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

# Set page layout and title
st.set_page_config(page_title="Flashman AI", page_icon="⚡", layout="wide")

# Sidebar for controls and info
with st.sidebar:
    st.title("⚡ Flashman AI")
    st.caption("Your straightforward AI assistant.")
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = [
            SystemMessage(content="You are a Straight forward Ai agent")
        ]
        st.rerun()
        
    st.divider()
    st.markdown("### About")
    st.info("Flashman is designed to give you quick, fast, and straightforward answers without the fluff.")

# Main Header
st.title("⚡ Flashman 1.0")
st.markdown("Welcome! I'm your straightforward AI agent. How can I help you today?")

# Initialize the model
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2506")

model = get_model()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a Straight forward Ai agent")
    ]

# Avatars for UI
USER_AVATAR = "👤"
BOT_AVATAR = "⚡"

# Display chat messages from history (excluding system message)
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown(message.content)

# React to user input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message in chat message container
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get assistant response
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        with st.spinner("Thinking... ⚡"):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)
            
    # Add assistant response to chat history
    st.session_state.messages.append(AIMessage(content=response.content))
