import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("HF_TOKEN")

from langchain_huggingface import  HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
model="openai/gpt-oss-20b"
llmhl=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model))

ls=[
    SystemMessage(content='please answer as is given in exmaples.'),
    HumanMessage(content='what is spoken in france'),
    AIMessage(content='French haha'),
    HumanMessage(content='what is spoken in india'),
    AIMessage(content='Hindi haha'),
]
ls.append(HumanMessage(content='what is spoken in Germany'))
res=llmhl.invoke(ls)
print(res.content)