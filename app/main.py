import ollama
from fastapi import FastAPI, UploadFile,File
from pydantic import BaseModel
from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.embedder import embed
from retrieval.vectorstore import store_documents
from retrieval.retriever import ask
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from retrieval.vectorstore import create_collection, get_client
import weaviate
from config.settings import (FILEPATH)
from pathlib import Path
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.weaviate_client = get_client()
    create_collection(app.state.weaviate_client)
    yield
    app.state.weaviate_client.close()
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)
class QueryRequest(BaseModel):
    question: str

@app.post("/api/upload")
async def upload_documents(file: UploadFile = File(...)):
    save_path = Path(FILEPATH) / Path(file.filename).name
    with open(save_path,"wb") as f:
        f.write(await file.read())
    text = load_pdf(save_path)
    chunks = chunk_text(text)
    embeddings =embed(chunks)
    store_documents(chunks,embeddings,app.state.weaviate_client,file.filename)
    return {"status":"success","message":f"Ingested{len(chunks)} chunks"}
@app.post("/api/chat")
async def chat_with_pdf(request:QueryRequest):
    result=ask(request.question, app.state.weaviate_client)
    sources = [
        {"source":chunk,"title":f"Source {i+1}","url":"#"}
        for i,chunk in enumerate(result["sources"])
    ]
    return {"reply":result["answer"],"sources":sources}
