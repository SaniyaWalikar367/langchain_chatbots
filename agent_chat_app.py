from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("HF_TOKEN")
api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=50)
wiki_tool=WikipediaQueryRun(api_wrapper=api_wrapper)
wikirep=wiki_tool.invoke({"query":"AI Agents"})
print(wikirep)
llm = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct"
    )
)

tools=[wiki_tool]
llm_with_tools=llm.bind_tools([wiki_tool])
result=llm.invoke("hello world")
print(result.content)
result2=llm.invoke("who  invented internet")
print(f" result2 is {result2}")