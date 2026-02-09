from langchain_community.utilities. sql_database import  SQLDatabase
from langchain_core import messages
sql_db=SQLDatabase.from_uri("sqlite:///SalesDB/sales.db")

from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
from langchain_community.agent_toolkits import SQLDatabaseToolkit


toolkit=SQLDatabaseToolkit(db=sql_db,llm=llm)
toolkit.get_tools()

from langchain.agents import create_agent

agent=create_agent(llm,toolkit.get_tools())
graph=agent.get_graph()
graph.print_ascii()

question="what is the  total sales of the Laptop ?"

for step in agent.stream(
    {"messages":[{"role":"user","content":question}]},stream_mode="values"
):
    step["messages"][-1].pretty_print()