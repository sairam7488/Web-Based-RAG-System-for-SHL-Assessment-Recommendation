# embeddings/search.py

import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embeddings
with open("embeddings/data/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

embeddings = data["embeddings"]
metadata = data["metadata"]

model = SentenceTransformer("all-MiniLM-L6-v2")

def search(query, top_k=5):
    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, embeddings)[0]
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "name": metadata[idx]["name"],
            "url": metadata[idx]["url"],
            "score": float(scores[idx])
        })

    return results

# Test
if __name__ == "__main__":
    query = "java programming test"
    results = search(query)

    for r in results:
        print(r)