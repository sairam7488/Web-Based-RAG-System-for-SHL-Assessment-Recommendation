# api/search_service.py

import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embeddings once (on app start)
with open("embeddings/data/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

EMBEDDINGS = data["embeddings"]
METADATA = data["metadata"]

MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def recommend_assessments(query: str, top_k: int = 5):
    query_vec = MODEL.encode([query])
    scores = cosine_similarity(query_vec, EMBEDDINGS)[0]

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "name": METADATA[idx]["name"],
            "url": METADATA[idx]["url"],
            "score": float(scores[idx])
        })

    return results