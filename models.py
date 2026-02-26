
from pydantic import BaseModel

class CodeAnalysis(BaseModel):
    complexity:str
    bugs:list[str]
    improvements:list[str]
    better_approaches:list[str]