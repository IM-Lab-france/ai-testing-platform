import os
from pydantic import BaseSettings

class Config(BaseSettings):
    # Paramètres de connexion à la base de données
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # Clés API pour les services externes
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    # Paramètres de sécurité
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

# Instanciation de la configuration
config = Config()