from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
class llm_schema(TypedDict):
    setup: str
    punchline:str
obj=llm_schema(**{"hello":"some setup","punchline":"some punchline"})
print(obj)