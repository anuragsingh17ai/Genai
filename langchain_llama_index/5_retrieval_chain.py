from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader

embeddings = SpacyEmbeddings(model_name='en_core_web_sm')
llm = Ollama(model='llama2')
loader = PDFPlumberLoader(r'/home/jellyfish/Simalarity/llms/documents/A1860-45.pdf')
docs = loader.load()

textSplitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap =100)
documents = textSplitter.split_documents(docs)
db  = FAISS.from_documents(documents,embeddings)

prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based on only provided context:
    <context>
    {context}
    </context>

    Question: {input}
"""
)

document_chain = create_stuff_documents_chain(llm,prompt)
retriever = db.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "what is llm ?"})

print(response["answer"])