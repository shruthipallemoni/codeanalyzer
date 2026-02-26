import os
from dotenv import load_dotenv
from models import CodeAnalysis
from langchain_groq import ChatGroq

load_dotenv() 

api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=api_key
)


model_with_structure=model.with_structured_output(CodeAnalysis)

def analyze_code(code:str):
    response=model_with_structure.invoke(
        f"Analyze the following code : \n{code}"
    )
    data = response.model_dump()

    if not data["bugs"]:
        data["bugs"] = ["No bugs found"]

    return data




