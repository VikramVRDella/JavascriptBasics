import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful coding assistant. Answer user queries clearly."),
        ("user", "Question: {question}")
    ]
)

# LLM
llm = ChatOllama(model="tinyllama:latest", temperature=0.3)
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser


# UI
st.title("Coding Assistant Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask a coding question...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = " "

        for chunk in chain.stream({"question": user_input}):
            full_response += chunk
            message_placeholder.markdown(full_response)

    # Save response
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )