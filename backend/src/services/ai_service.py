import importlib
from sqlalchemy.orm import Session
from src.db.models import AIProvider
from src.core.security import decrypt_api_key, encrypt_api_key

class AIProviderService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self._providers_cache = {}

    async def get_provider(self, provider_id: int):
        """
        Récupère un fournisseur d'IA par son ID.

        - **provider_id**: L'identifiant du fournisseur à récupérer.

        Retourne une instance du fournisseur d'IA.
        """
        if provider_id in self._providers_cache:
            return self._providers_cache[provider_id]

        provider_data = await self.db_session.get(AIProvider, provider_id)
        if not provider_data:
            raise ValueError(f"Provider {provider_id} not found")

        # Importation dynamique du module
        module = importlib.import_module(provider_data.module_path)
        provider_class = getattr(module, provider_data.class_name)

        # Décryptage de la clé API
        api_key = decrypt_api_key(provider_data.api_key)

        # Instanciation du fournisseur
        provider = provider_class(api_key=api_key, config=provider_data.config)
        self._providers_cache[provider_id] = provider
        return provider

    async def register_provider(self, provider_data: dict):
        """
        Enregistre un nouveau fournisseur d'IA.

        - **provider_data**: Les données du fournisseur à enregistrer.

        Retourne l'instance du fournisseur enregistré.
        """
        provider = AIProvider(
            name=provider_data['name'],
            description=provider_data['description'],
            api_url=provider_data['api_url'],
            module_path=provider_data['module_path'],
            class_name=provider_data['class_name'],
            api_key=encrypt_api_key(provider_data['api_key']),
            config=provider_data['config']
        )
        self.db_session.add(provider)
        await self.db_session.commit()
        await self.db_session.refresh(provider)
        return provider