# Web-Based-RAG-System-for-SHL-Assessment-Recommendation
SHL GenAI – RAG Assessment Recommender

1. Project Overview
This project is a web-based Retrieval-Augmented Generation (RAG) system designed to recommend suitable SHL assessments based on a user’s natural language query. The system uses semantic embeddings instead of keyword matching to understand user intent.

2. Objective
The objective is to build a GenAI-powered solution that understands natural language queries, retrieves relevant SHL assessments semantically, and provides ranked recommendations through a web API.

3. System Workflow
1. SHL assessment data is collected and stored in JSON format.
2. Each assessment is converted into a semantic embedding.
3. User queries are converted into embeddings.
4. Cosine similarity is used to compare embeddings.
5. The most relevant assessments are returned as recommendations.

4. Technologies Used
Python 3.9+, FastAPI, Uvicorn, SentenceTransformers, scikit-learn, NumPy, Requests, BeautifulSoup.

5. Project Structure
api/, scraper/, embeddings/, data/, run_server.py, requirements.txt, .gitignore.

6. Step-by-Step Execution
Step 1: Clone the repository
git clone <repo_url>

Step 2: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Scrape SHL data
python scraper/scrape_shl.py

Step 5: Generate embeddings
python embeddings/build_embeddings.py

Step 6: Start API server
python run_server.py

7. API Endpoints
GET /health – Health check
POST /recommend – Get assessment recommendations

8. Conclusion
This project demonstrates an end-to-end GenAI RAG system covering data collection, embedding generation, semantic retrieval, and API deployment.
