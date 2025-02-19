from fastapi.testclient import TestClient
from src.main import app  # Assurez-vous que votre application FastAPI est importée ici

client = TestClient(app)

def test_run_campaign_success():
    response = client.post("/campaigns/1/run")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Campaign started successfully"

def test_run_campaign_failure():
    response = client.post("/campaigns/999/run")  # Assurez-vous que l'ID 999 n'existe pas
    assert response.status_code == 500
    data = response.json()
    assert "detail" in data