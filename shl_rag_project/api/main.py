from fastapi import FastAPI
from pydantic import BaseModel
from api.search_service import recommend_assessments

app = FastAPI(title="SHL RAG Recommender")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(req: QueryRequest):
    results = recommend_assessments(req.query, req.top_k)
    return {
        "query": req.query,
        "recommendations": results
    }