import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
weaviate_url = os.getenv("weaviate_url")
CHUNK_SIZE= int(os.getenv("chunk_size", "1000"))
CHUNK_OVERLAP = int(os.getenv("chunk_overlap", "200"))
TOP_K = int(os.getenv("top_k", "5"))
FILEPATH = os.getenv("FILEPATH")