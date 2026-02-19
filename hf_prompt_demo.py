import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("HF_TOKEN")

from langchain_huggingface import  HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
model="openai/gpt-oss-20b"
llmhl=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model))

#llmhl.invoke("what is the capital of France?")
prompt=ChatPromptTemplate.from_messages([("user", "{inp}"),('system','Answer in just one word.')])
chain=prompt|llmhl

res=chain.invoke({"inp":"what is the capital of France?"})
print(res.content)

