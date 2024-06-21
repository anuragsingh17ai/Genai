from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import SpacyTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

llm = Ollama(model='llama2')
loader =  PDFPlumberLoader(r'/home/jellyfish/Simalarity/llms/documents/A1860-45.pdf')
docs = loader.load()

text_splitter = SpacyTextSplitter(chunk_size = 1000, chunk_overlap = 100)
documents = text_splitter.split_documents(docs)

embedding = SpacyEmbeddings(model_name='en_core_web_sm')

vector = FAISS.from_documents(documents,embedding)
retriever = vector.as_retriever()

prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"You are India's top lawyer"),
        ('user',"Answer the following  based on the provided context only \n\n <context>\n{context}\n </context"),
        ('user','{input}')
    ]
)

document_chain = create_stuff_documents_chain(llm,prompt)
retrieval_chain = create_retrieval_chain(retriever,document_chain)

response = retrieval_chain.invoke({'input':"what is the punishement for robbery in indian law"})

print(response['answer'])