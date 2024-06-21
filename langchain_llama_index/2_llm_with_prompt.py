from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model='llama2',temperature=0.5)
outputParser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are India's top lawyer Mr. Anurag."),
        ("user", "{input}")
    ]
)

chain = prompt | llm | outputParser

output = chain.invoke({"input": "who is the chief justice of india ?"})
print(output)
