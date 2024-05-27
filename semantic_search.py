# semantic_search.py

from transformers import AutoTokenizer, AutoModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sqlite3

class SemanticSearch:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModel.from_pretrained("bert-base-uncased")

    def generate_embedding(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        return embeddings

    def search_documents(self, query_embedding):
        conn = sqlite3.connect('documents.db')
        c = conn.cursor()
        c.execute("SELECT id, title, industry, geography, use_case, embedding FROM documents")
        rows = c.fetchall()
        conn.close()

        documents = []
        for row in rows:
            doc_embedding = np.frombuffer(row[5], dtype=np.float32)
            similarity = cosine_similarity([query_embedding], [doc_embedding])[0][0]
            documents.append((row[1], similarity))

        documents.sort(key=lambda x: x[1], reverse=True)
        return [doc[0] for doc in documents[:5]]  # Return top 5 results
