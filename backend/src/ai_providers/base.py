from abc import ABC, abstractmethod

class BaseAIProvider(ABC):
    def __init__(self, api_key: str, config: dict):
        """
        Initialise le fournisseur d'IA avec une clé API et une configuration.

        - **api_key**: La clé API pour accéder au service du fournisseur d'IA.
        - **config**: La configuration spécifique au fournisseur d'IA.
        """
        self.api_key = api_key
        self.config = config

    @abstractmethod
    async def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse à partir d'un prompt donné.

        - **prompt**: Le texte d'entrée pour lequel générer une réponse.

        Retourne un dictionnaire contenant :
        {
            'response': str,
            'tokens': int,
            'time': float
        }
        """
        pass

    @abstractmethod
    async def count_tokens(self, text: str) -> int:
        """
        Compte le nombre de tokens dans un texte donné.

        - **text**: Le texte pour lequel compter les tokens.

        Retourne le nombre de tokens.
        """
        pass