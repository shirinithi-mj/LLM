from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
prompt_template=ChatPromptTemplate.from_messages({
    ("system","you are a helpful assistant"),
    ("human","{input}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
str_parser=StrOutputParser()
def dictionary_maker(text:str)->dict:
    return{"text":text}
dictionary_maker_runnable=RunnableLambda(dictionary_maker)
prompt_post=ChatPromptTemplate.from_messages({
    ("system","you are a social media post generator"),
    ("human","create a post for the following text for Linkedin:{text}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
str_parser=StrOutputParser()
chain=prompt_template|llm|str_parser|dictionary_maker_runnable|prompt_post|llm|str_parser
response=chain.invoke({"what is the capital of france"})
print(response)