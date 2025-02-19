import pytest
from sqlalchemy.orm import Session
from src.services.ai_service import AIProviderService
from src.db.models import AIProvider
from src.core.security import encrypt_api_key

@pytest.fixture
def mock_db_session():
    # Mock de la session de base de données
    class MockSession:
        async def get(self, model, ident):
            # Retourne un fournisseur fictif pour l'ID 1
            if ident == 1:
                return AIProvider(
                    id=1,
                    name="MockProvider",
                    module_path="mock.provider",
                    class_name="MockProvider",
                    api_key=encrypt_api_key("mock_api_key"),
                    config={}
                )
            return None

        async def add(self, instance):
            pass

        async def commit(self):
            pass

        async def refresh(self, instance):
            pass

    return MockSession()

@pytest.mark.asyncio
async def test_get_provider_success(mock_db_session):
    service = AIProviderService(mock_db_session)
    provider = await service.get_provider(1)
    assert provider is not None
    assert provider.name == "MockProvider"

@pytest.mark.asyncio
async def test_get_provider_failure(mock_db_session):
    service = AIProviderService(mock_db_session)
    with pytest.raises(ValueError):
        await service.get_provider(999)

@pytest.mark.asyncio
async def test_register_provider(mock_db_session):
    service = AIProviderService(mock_db_session)
    provider_data = {
        "name": "NewProvider",
        "description": "New Provider",
        "api_url": "https://api.newprovider.com",
        "module_path": "new.provider",
        "class_name": "NewProvider",
        "api_key": "new_api_key",
        "config": {}
    }
    provider = await service.register_provider(provider_data)
    assert provider.name == "NewProvider"