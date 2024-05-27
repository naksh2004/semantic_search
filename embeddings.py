# embeddings.py

from sentence_transformers import SentenceTransformer

# Initialize SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to generate embeddings
def generate_embedding(text):
    return model.encode(text)
