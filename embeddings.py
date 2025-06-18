import json
import random

VOCAB = ["king", "queen", "crown", "royal", "throne", "hat"]
DIM = 2
RANGE = (-1, 1)

embeddings = {
        word: {
            "v": [round(random.uniform(*RANGE), 2) for _ in range (DIM)],
            "u": [round(random.uniform(*RANGE), 2) for _ in range (DIM)]
            }
        for word in VOCAB
        }

with open("embeddings.json", "w") as f:
    json.dump(embeddings, f, indent=2)

print("Initial embeddings saved to embeddings.json")
