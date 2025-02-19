import openai
import time
from src.ai_providers.base import BaseAIProvider

class ChatGPTProvider(BaseAIProvider):
    def __init__(self, api_key: str, config: dict):
        """
        Initialise le fournisseur ChatGPT avec une clé API et une configuration.

        - **api_key**: La clé API pour accéder au service de ChatGPT.
        - **config**: La configuration spécifique au fournisseur ChatGPT.
        """
        super().__init__(api_key, config)
        openai.api_key = api_key

    async def generate_response(self, prompt: str) -> dict:
        """
        Génère une réponse à partir d'un prompt donné en utilisant l'API de ChatGPT.

        - **prompt**: Le texte d'entrée pour lequel générer une réponse.

        Retourne un dictionnaire contenant :
        {
            'response': str,
            'tokens': int,
            'time': float
        }
        """
        start_time = time.time()
        response = await openai.ChatCompletion.create(
            model=self.config.get('model', 'gpt-3.5-turbo'),
            messages=[{"role": "user", "content": prompt}]
        )
        end_time = time.time()

        return {
            'response': response.choices[0].message.content,
            'tokens': response.usage.total_tokens,
            'time': end_time - start_time
        }

    async def count_tokens(self, text: str) -> int:
        """
        Compte le nombre de tokens dans un texte donné en utilisant l'API de ChatGPT.

        - **text**: Le texte pour lequel compter les tokens.

        Retourne le nombre de tokens.
        """
        response = await openai.Completion.create(
            model=self.config.get('model', 'gpt-3.5-turbo'),
            prompt=text,
            max_tokens=0
        )
        return response.usage.total_tokens