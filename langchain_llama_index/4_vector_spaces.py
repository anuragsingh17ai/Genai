from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from  langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma


raw_documents = TextLoader('/home/jellyfish/Simalarity/llms/documents/iky').load()
text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap=10)
documents = text_splitter.split_documents(raw_documents)


embedder = SpacyEmbeddings()
db = Chroma.from_documents(documents,embedder)

query = "what is llm ? "

# docs = db.similarity_search(query)
# # print(docs[2].page_content)


# ## we can also convert our query into vector then search it in vector space

# query_embedder = embedder.embed_query(query)

# docs = db.similarity_search_by_vector(query_embedder)
# print(docs[0].page_content)

# ## Maximum marginal relevance search
# embedder_query = embedder.embed_query(query)
# found_docs =db.similarity_search_by_vector_with_relevance_scores(embedder_query,k=2)
# print(found_docs)
