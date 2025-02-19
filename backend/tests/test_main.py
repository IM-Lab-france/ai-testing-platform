from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AI Testing Platform"}

def test_ai_providers_route():
    response = client.get("/api/providers/")
    assert response.status_code == 200

def test_campaigns_route():
    response = client.get("/api/campaigns/")
    assert response.status_code == 200