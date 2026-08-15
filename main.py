from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="RAG Backend API")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/retrieve")
def retrieve_context(request: QueryRequest):
    # In production, this connects to a Vector DB (e.g., Pinecone/Milvus)
    simulated_db = [
        "Chunk 1: RAG combines retrieval and generation.",
        "Chunk 2: Vector embeddings power semantic search.",
        "Chunk 3: Cross-encoders provide accurate re-ranking."
    ]
    return {
        "query": request.query,
        "results": simulated_db[:request.top_k]
    }