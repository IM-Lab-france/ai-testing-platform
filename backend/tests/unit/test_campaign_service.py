import pytest
from sqlalchemy.orm import Session
from src.services.campaign_service import CampaignService
from src.services.ai_service import AIProviderService
from src.db.models import Campaign, Question, CampaignResult

@pytest.fixture
def mock_db_session():
    # Mock de la session de base de données
    class MockSession:
        async def get(self, model, ident):
            # Retourne une campagne fictive pour l'ID 1
            if model == Campaign and ident == 1:
                return Campaign(
                    id=1,
                    questions=[1, 2],
                    config={'providers': [1]}
                )
            return None

        async def query(self, *args, **kwargs):
            # Retourne des questions fictives
            return [Question(id=1, content="Test question")]

        async def add(self, instance):
            pass

        async def commit(self):
            pass

    return MockSession()

@pytest.fixture
def mock_ai_service():
    # Mock du service AIProviderService
    class MockAIProviderService:
        async def get_provider(self, provider_id):
            class MockProvider:
                async def generate_response(self, prompt):
                    return {'response': 'Mock response', 'tokens': 10, 'time': 0.5}
            return MockProvider()

    return MockAIProviderService()

@pytest.mark.asyncio
async def test_run_campaign_success(mock_db_session, mock_ai_service):
    service = CampaignService(mock_db_session, mock_ai_service)
    await service.run_campaign(1)
    # Vérifiez que les résultats sont ajoutés à la session
    assert len(mock_db_session.new) == 1

@pytest.mark.asyncio
async def test_run_campaign_failure(mock_db_session, mock_ai_service):
    service = CampaignService(mock_db_session, mock_ai_service)
    with pytest.raises(ValueError):
        await service.run_campaign(999)