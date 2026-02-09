from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
str_parser = StrOutputParser()
def dictionary_maker(text: str):
    return {"topic": text}
dictionary_maker_runnable = RunnableLambda(dictionary_maker)
def linkedin_good_news(text: dict):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional LinkedIn content writer."),
        (
            "human",
            "Write a LinkedIn post about GOOD news related to {topic}. "
            "Keep it professional and optimistic. Limit to 5 lines."
        )
    ])
    return (prompt | llm | str_parser).invoke(text)
def linkedin_bad_news(text: dict):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional LinkedIn content writer."),
        (
            "human",
            "Write a LinkedIn post about BAD news related to {topic}. "
            "Keep it professional and empathetic. Limit to 5 lines."
        )
    ])
    return (prompt | llm | str_parser).invoke(text)
def instagram_good_news(text: dict):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Instagram content creator."),
        (
            "human",
            "Write an Instagram post sharing GOOD news about {topic}. "
            "Make it fun, emotional, and engaging. Limit to 5 short lines."
        )
    ])
    return (prompt | llm | str_parser).invoke(text)
def instagram_bad_news(text: dict):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Instagram storyteller."),
        (
            "human",
            "Write an Instagram post sharing BAD news about {topic}. "
            "Make it emotional and relatable. Limit to 5 short lines."
        )
    ])
    return (prompt | llm | str_parser).invoke(text)
linkedin_good_runnable = RunnableLambda(linkedin_good_news)
linkedin_bad_runnable = RunnableLambda(linkedin_bad_news)
instagram_good_runnable = RunnableLambda(instagram_good_news)
instagram_bad_runnable = RunnableLambda(instagram_bad_news)
prompt_template = ChatPromptTemplate.from_messages([
    ("human", "{topic}")
])
final_chain = (
    prompt_template
    | llm
    | str_parser
    | dictionary_maker_runnable
    | RunnableParallel(
        linkedin_good=linkedin_good_runnable,
        linkedin_bad=linkedin_bad_runnable,
        instagram_good=instagram_good_runnable,
        instagram_bad=instagram_bad_runnable
    )
)
if __name__ == "__main__":
    response = final_chain.invoke({"topic": "car rides"})
    print(response)