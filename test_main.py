from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_retrieve_context():
    response = client.post("/api/retrieve", json={"query": "What is RAG?", "top_k": 2})
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) == 2