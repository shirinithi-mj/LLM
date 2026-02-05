from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
response=llm.invoke("tell me a story.Generate output in akey value pair")
print(response.content)