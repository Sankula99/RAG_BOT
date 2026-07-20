from langchain_ollama import OllamaEmbeddings
from config.settings import EMBEDDING_MODEL

def get_embedder():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)
def embed(chunks):
    embedder = get_embedder()
    return embedder.embed_documents(chunks)

def create_query_embeddings(query):
    embedder = get_embedder()
    return embedder.embed_query(query)