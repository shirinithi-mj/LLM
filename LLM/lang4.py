from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=1)
user_input=input("enter a topic:")
fixed_prompt=PromptTemplate.from_template("write a riddle about{topic}")
ready_prompt=fixed_prompt.invoke({"topic":user_input})
response=llm.invoke(ready_prompt)
print(response.content)
