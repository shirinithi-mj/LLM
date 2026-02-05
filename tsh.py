from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel,Field
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
class llm_schema(BaseModel):
    tone:str=Field(description="The style of the writing")
    story:str=Field(description="The creative content")
    Hightlight:str=Field(description="key takeaway")
llm_structured_output=llm.with_structured_output(llm_schema)
response=llm_structured_output.invoke("tell me a joke")
print(response)
print(type(response))