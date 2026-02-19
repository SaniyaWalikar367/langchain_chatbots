from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv("HF_TOKEN")

from langchain_huggingface import  HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
model="openai/gpt-oss-20b"
llmhl=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model))

prompt=ChatPromptTemplate.from_template(
    "Explain {topic} in one sentence,formatted as JSON with single key named Quantun Computing'."
)
Jsonp=JsonOutputParser()
chain=prompt|llmhl|Jsonp
result=chain.invoke({"topic":"what is quantum computing "})
print(result)