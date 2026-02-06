from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableBranch
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
parser=StrOutputParser()
classifier_prompt=ChatPromptTemplate.from_messages({
    ("system","Answer only POSITIVE or NEGATIVE"),
    ("human","{text}")
})
classifier_chain=classifier_prompt|llm|parser
def classify(text):
    sentiment=classifier_chain.invoke({"text":text}).strip().upper()
    return{
        "text":text,
        "sentiment":sentiment
    }
classify_runnable=RunnableLambda(classify)
positive_chain=RunnableLambda(
    lambda x: f"POSITIVE REVIEW:{x['text']}"
    )
negative_chain=RunnableLambda(
    lambda x: f"NEGATIVE REVIEW:{x['text']}"
    )
conditional_chain=RunnableBranch(
    (lambda x: x["sentiment"]=="POSITIVE",positive_chain),
     (lambda x: x["sentiment"]=="NEGATIVE",negative_chain),
     RunnableLambda(lambda x:"Unknown sentiment")
    )
final_chain=classify_runnable|conditional_chain
print(final_chain.invoke("The movie was amazing and emotional"))
print(final_chain.invoke("The movie was boring and slow"))