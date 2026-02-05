from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=1)
user_input=input("enter a topic:")
user_tone=input("enter a tone:")
prompt_template=ChatPromptTemplate.from_messages([
    ("system", "you are{tone} person"),
    ("user","give a fun fact about{topic}")

])
prompt_given=prompt_template.invoke({
    "topic":user_input,
    "tone":user_tone
})
response=llm.invoke(prompt_given).content
print(response)