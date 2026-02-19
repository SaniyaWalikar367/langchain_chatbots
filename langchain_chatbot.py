import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("HF_TOKEN")

from langchain_huggingface import  HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
model="openai/gpt-oss-20b"
llmhl=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model))

ls=[SystemMessage(content='please answer all the questions .')]

ls.append(HumanMessage(content='what is the capital of india?'))
res=llmhl.invoke(ls)
ls.append(AIMessage(content=res.content))
ls.append(HumanMessage(content='what is spoken in india?'))
res=llmhl.invoke(ls)
ls.append(AIMessage(content=res.content))
ls.append(HumanMessage(content='what is famous food in india?'))
res=llmhl.invoke(ls)
ls.append(AIMessage(content=res.content))
ls.append(HumanMessage(content='what was i talking about?'))


res=llmhl.invoke(ls)

print(res.content)