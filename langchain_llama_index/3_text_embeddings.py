from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
embedder = SpacyEmbeddings(model_name='en_core_web_sm')

embeddings = embedder.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)

embedded_query = embedder.aembed_query("what was the name mentioned ?") # converted into vectors