from ingestion.embedder import embed
from ingestion.embedder import create_query_embeddings
import weaviate
import ollama
from config.settings import(OLLAMA_MODEL, TOP_K,)

def ask(question,client, llm_model = OLLAMA_MODEL, top_k = TOP_K):
  query_embeddings = create_query_embeddings(question)

  collection = client.collections.get("Documents")
  response = collection.query.near_vector(
      near_vector =query_embeddings,
      limit=top_k
    )
  retrieved_chunks =[obj.properties["content"]for obj in response.objects]
 
  context ="\n\n".join(retrieved_chunks)
  prompt =f"""Answer the question based on the context below. If the answer isn't in the context, say so.
  Context:{context}
  Question:{question}
  Answer:"""
  response = ollama.generate(model=llm_model,prompt =prompt)
  return{
    "answer":response["response"],
    "sources": retrieved_chunks
  }