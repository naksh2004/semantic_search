from pymongo import MongoClient
import re

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['documents_db']
collection = db['documents']

# Function to save document to database
def save_to_database(text, embedding):
    document = {"text": text, "embedding": embedding.tolist()}
    collection.insert_one(document)

# Function to retrieve all documents from the database
def get_all_documents():
    return list(collection.find())

# Function to extract first non-blank sentence from text
def extract_first_non_blank_sentence(text):
    newline_index = text.find('\n')
    if newline_index != -1:
        return text[:newline_index].strip()
    else:
        return text.strip()

# Function to extract text after "Customer Stories"
def extract_after_customer_stories(text):
    pattern = r"customer stories / (.*)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None
