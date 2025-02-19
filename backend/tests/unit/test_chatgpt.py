import pytest
from unittest.mock import patch, AsyncMock
from src.ai_providers.chatgpt import ChatGPTProvider

@pytest.fixture
def mock_chatgpt_provider():
    # Mock de la clé API et de la configuration
    api_key = "mock_api_key"
    config = {"model": "gpt-3.5-turbo"}
    return ChatGPTProvider(api_key, config)

@pytest.mark.asyncio
async def test_generate_response(mock_chatgpt_provider):
    # Mock de la réponse de l'API de ChatGPT
    with patch('openai.ChatCompletion.create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = {
            "choices": [{"message": {"content": "Mock response"}}],
            "usage": {"total_tokens": 10}
        }
        response = await mock_chatgpt_provider.generate_response("Test prompt")
        assert response['response'] == "Mock response"
        assert response['tokens'] == 10
        assert 'time' in response

@pytest.mark.asyncio
async def test_count_tokens(mock_chatgpt_provider):
    # Mock de la réponse de l'API de ChatGPT
    with patch('openai.Completion.create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value = {
            "usage": {"total_tokens": 5}
        }
        tokens = await mock_chatgpt_provider.count_tokens("Test text")
        assert tokens == 5