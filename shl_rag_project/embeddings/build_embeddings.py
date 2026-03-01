# embeddings/build_embeddings.py

import json
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load data
with open("data/raw/shl_catalog.json", "r", encoding="utf-8") as f:
    assessments = json.load(f)

texts = []
metadata = []

for item in assessments:
    text = f"{item['name']} {item['description']}"
    texts.append(text)
    metadata.append(item)

print(f"Loaded {len(texts)} assessments")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

# Save embeddings
with open("embeddings/data/embeddings.pkl", "wb") as f:
    pickle.dump({
        "embeddings": embeddings,
        "metadata": metadata
    }, f)

print("Embeddings saved to embeddings/data/embeddings.pkl")