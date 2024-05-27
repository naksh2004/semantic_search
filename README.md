Semantic Search System

This repository contains a semantic search system built using FastAPI in Python. The system allows users to upload case study documents related to a fictitious company, MindTickle, and perform semantic search queries to retrieve relevant case study names.

Objective

The main objective of this project is to develop a web application that implements semantic search on case study documents. The system prioritizes relevant results based on meaning and context, rather than just exact keyword matches. Additionally, the system integrates a Large Language Model (LLM) to enhance search accuracy.

Features

Upload API: Allows users to upload case study documents in PDF format.
Semantic Search API: Enables users to perform semantic search queries to retrieve relevant case study names.
LLM Integration: Integrates a Large Language Model (LLM) to enhance search accuracy by optimizing queries for industry, use case, and geography.

How to Use

Installation
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/semantic-search.git
cd semantic-search
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Start the FastAPI application:
bash
Copy code
uvicorn main:app --reload
Access the application in your web browser at http://localhost:8000.

Use the provided APIs to upload case study documents and perform semantic search queries.

API Endpoints

POST /upload: Uploads a new case study document in PDF format.
GET /search: Performs a semantic search query and returns relevant case study names.
LLM Integration
The system integrates a Large Language Model (LLM) to improve search accuracy. LLMs are used to optimize queries for industry, use case, and geography, enhancing the relevance of search results.

