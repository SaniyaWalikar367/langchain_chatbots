from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import  HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.runnables import RunnableWithMessageHistory

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("HF_TOKEN")

model="openai/gpt-oss-20b"
llm_hf=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model))

prompt=ChatPromptTemplate.from_messages([
    ("system","you are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])
chain=prompt|llm_hf


store={}
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]

superchain=RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
response1=superchain.invoke(
    {"input":"hi,my name is David Jhonson"},config={"configurable":{"session_id":"david"}}
    )
response2=superchain.invoke(
    {"input":"what is my name?"},config={"configurable":{"session_id":"david"}}
    )   
print(response2.content)