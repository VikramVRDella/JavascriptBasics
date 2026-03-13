from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

#prompt

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful coding assistant.answer users queries"),
        ("user", "Question:{question}")
    ]
)


#Streamlit 
st.title("Sample Chat Bot")
input_text = st.text_input("Search what you want:")

#llm
llm = ChatOllama(temperature=0.3,model="tinyllama:latest")
output_parser = StrOutputParser()

chain = prompt | llm |output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))