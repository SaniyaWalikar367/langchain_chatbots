import os
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv("HF_TOKEN"))
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
model="openai/gpt-oss-20b"
hflm=ChatHuggingFace(llm = HuggingFaceEndpoint(repo_id=model))
result=hflm.invoke("what is spoken in dubai?")
import streamlit as st
st.write(result.content)