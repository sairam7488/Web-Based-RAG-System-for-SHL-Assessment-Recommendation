import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/raw/shl_catalog.json") as f:
    data = json.load(f)

texts = []
metadata = []

for item in data:
    text = f"{item['name']} {item['description']} Test Type {' '.join(item['test_type'])}"
    texts.append(text)
    metadata.append(item)

embeddings = model.encode(texts, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "data/processed/faiss.index")

with open("data/processed/metadata.json", "w") as f:
    json.dump(metadata, f)

print("Embedding index created")