import chromadb
chroma_client = chromadb.PersistentClient('/home/jellyfish/llms/vector_database/storage')
collection = chroma_client.create_collection(name='my_collection')
collection.add(
    documents=["This is a document","This ia another document"],
    metadatas = [ {"source": "my_source"},{"source":"my_source"}],
    ids=['id1','id2']
)

results = collection.query(
    query_texts=["this is a query document"],
    n_results=2
)

print(results)
