from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model= "llama2")
output = llm.invoke('how are you bro ? I am learning to use you well so that we that help of you we can bring improvement to society.')
print(output)

