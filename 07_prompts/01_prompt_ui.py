
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

st.header("Research Tool")

llm=ChatOpenAI(model="gpt-5.2-pro-2025-12-11")

user_input=st.text_input("Enter your prompt ")

if st.button("Summarize"):
    result=llm.invoke(user_input)
    st.write(result.text)


