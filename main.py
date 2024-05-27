from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
import logging
from sentence_transformers import SentenceTransformer
from database import save_to_database, get_all_documents, extract_first_non_blank_sentence, extract_after_customer_stories

# Initialize FastAPI app
app = FastAPI()

# Initialize SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to generate embeddings
def generate_embedding(text):
    return model.encode(text)

# Endpoint to upload a document
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    text_after_customer_stories = extract_after_customer_stories(text)
    if text_after_customer_stories:
        embedding = generate_embedding(text_after_customer_stories)
        save_to_database(text_after_customer_stories, embedding)
        logging.info(f"Uploaded document: {text_after_customer_stories[:100]}")
        logging.info(f"Generated embedding: {embedding[:5]}")  # Log first 5 elements for brevity
    else:
        logging.warning("No 'Customer Stories' section found in the document")
    return {"message": "Document uploaded successfully"}

# Endpoint to search documents
@app.get("/search")
async def search_documents(q: str):
    query_embedding = generate_embedding(q)
    logging.info(f"Query embedding: {query_embedding[:5]}")  # Log first 5 elements for brevity
    documents = get_all_documents()
    similarities = []
    for doc in documents:
        if 'embedding' not in doc:
            continue  # Skip documents without embeddings
        doc_embedding = np.array(doc['embedding'])
        similarity = np.dot(query_embedding, doc_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding))
        similarities.append((doc['text'], similarity))
        logging.info(f"Document: {doc['text'][:100]}")
        logging.info(f"Similarity: {similarity}")
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_results = [extract_first_non_blank_sentence(result[0]) for result in similarities[:10]]
    return JSONResponse(content={"results": top_results})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
