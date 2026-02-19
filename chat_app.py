import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

model_id = "openai/gpt-oss-20b"  # Ensure this model ID is correct/available
hflm = ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model_id))
inp = st.text_input("Enter your name")
bt = st.button("Submit")
if bt:
    result = hflm.invoke(inp)
    st.write("result", result.content)



