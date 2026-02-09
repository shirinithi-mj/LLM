from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda
prompt_template=ChatPromptTemplate.from_messages({
    ("system","you are a movie summarizer"),
    ("human","summarize the movie in brief:{input}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
str_parser=StrOutputParser()
def dictionary_maker(text:str)->dict:
    return{"text":text}
dictionary_maker_runnable=RunnableLambda(dictionary_maker)
linkedin_prompt=ChatPromptTemplate.from_messages({
      ("system","you are a linkedin post generator"),
      ("human","create a post for the following text for linkedin:{text}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
str_parser=StrOutputParser()
chain_linkedin=linkedin_prompt|llm|str_parser
def insta_chain(text:dict):
    insta_prompt=ChatPromptTemplate.from_messages({
    ("system","you are a linkedin post generator"),
    ("human","create a post for the following text for Linkedin:{text}")
})
    llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
    str_parser=StrOutputParser()
    chain_insta=insta_prompt|llm|str_parser
    result=chain_insta.invoke(text)
    return result
insta_chain_runnable=RunnableLambda(insta_chain)
final_chain=(
    prompt_template|
    llm|
    str_parser|
    dictionary_maker_runnable|
    RunnableParallel(branches={"linkedin":chain_linkedin,"instagram":insta_chain})
    )
response=final_chain.invoke("KGF")
print(response)