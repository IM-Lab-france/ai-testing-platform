import pytest
from src.ai_providers.base import BaseAIProvider

def test_base_ai_provider_abstract_methods():
    # Vérifie que BaseAIProvider est une classe abstraite
    assert issubclass(BaseAIProvider, ABC)

    # Vérifie que les méthodes sont abstraites
    with pytest.raises(TypeError):
        # Tentative d'instanciation d'une classe abstraite
        BaseAIProvider(api_key="dummy_key", config={})

    # Vérifie que generate_response est une méthode abstraite
    assert BaseAIProvider.generate_response.__isabstractmethod__

    # Vérifie que count_tokens est une méthode abstraite
    assert BaseAIProvider.count_tokens.__isabstractmethod__