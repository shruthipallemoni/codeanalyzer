from fastapi import FastAPI
from pydantic import BaseModel
from llm import analyze_code

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/analyze")
def analyze(request: CodeRequest):
    result = analyze_code(request.code)
    return result

