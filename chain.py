from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt_template=ChatPromptTemplate.from_messages({
    ("system","you are a helpful assistant"),
    ("human","{input}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
str_parser=StrOutputParser()
chain=prompt_template|llm|str_parser
response=chain.invoke({"input":"what is the capital of france"})
print(response)