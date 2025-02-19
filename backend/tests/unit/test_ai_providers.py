import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assurez-vous que votre application FastAPI est importée ici

client = TestClient(app)

def test_create_provider():
    response = client.post("/providers/", json={
        "name": "TestProvider",
        "description": "Provider for testing",
        "api_url": "https://api.testprovider.com",
        "module_path": "src.ai_providers.test_provider",
        "class_name": "TestProvider",
        "api_key": "test_api_key",
        "config": {}
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TestProvider"

def test_list_providers():
    response = client.get("/providers/")
    assert response.status_code == 200
    providers = response.json()
    assert isinstance(providers, list)