from unittest import result
from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()
result = search.invoke("Obama's first name")
print(result)