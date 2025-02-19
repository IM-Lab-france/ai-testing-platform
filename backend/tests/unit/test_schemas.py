import pytest
from pydantic import ValidationError
from src.db.schemas import AIProviderCreate, QuestionCreate, CampaignCreate, CampaignResultCreate

def test_ai_provider_create_valid():
    data = {
        "name": "TestProvider",
        "api_url": "http://test.com",
        "module_path": "test.module",
        "class_name": "TestClass",
        "api_key": "test_key"
    }
    ai_provider = AIProviderCreate(**data)
    assert ai_provider.name == "TestProvider"

def test_ai_provider_create_invalid():
    data = {
        "name": "",  # Nom trop court
        "api_url": "invalid_url",
        "module_path": "test.module",
        "class_name": "TestClass",
        "api_key": "test_key"
    }
    with pytest.raises(ValidationError):
        AIProviderCreate(**data)

def test_question_create_valid():
    data = {
        "content": "Test question",
        "category": "Test",
        "tags": ["tag1", "tag2"]
    }
    question = QuestionCreate(**data)
    assert question.content == "Test question"

def test_campaign_create_valid():
    data = {
        "name": "Test Campaign",
        "status": "pending"
    }
    campaign = CampaignCreate(**data)
    assert campaign.name == "Test Campaign"

def test_campaign_result_create_valid():
    data = {
        "campaign_id": 1,
        "question_id": 1,
        "ai_provider_id": 1,
        "response": "Test response",
        "tokens_count": 10,
        "response_time": 0.5
    }
    result = CampaignResultCreate(**data)
    assert result.response == "Test response"