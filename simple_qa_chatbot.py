import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
#enviroment variables call
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


# creating chatbot
prompt = ChatPromptTemplate.from_messages([
    ('system','You are a helpful assistant.Please provide response to the user queries.'),
    ('user',"Question:{question}")
])

# streamlit framework
st.title('Simple LangChain Chatbot With GROQ API')
input_text = st.text_input('Search Any Thing You Want')

# openai LLM Call
llm = ChatGroq(model="llama-3.1-8b-instant")
output_parser = StrOutputParser()

# chain
chain = prompt | llm | output_parser
if input_text:
    st.write(chain.invoke({"question": input_text}))