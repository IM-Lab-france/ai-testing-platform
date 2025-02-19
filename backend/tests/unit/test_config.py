import os
import pytest
from src.core.config import Config

def test_config_defaults():
    # Vérifie les valeurs par défaut
    config = Config()
    assert config.DATABASE_URL == "sqlite:///./test.db"
    assert config.OPENAI_API_KEY == ""
    assert config.SECRET_KEY == "default_secret_key"
    assert config.ALGORITHM == "HS256"
    assert config.ACCESS_TOKEN_EXPIRE_MINUTES == 30

def test_config_from_env(monkeypatch):
    # Définit des variables d'environnement pour le test
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:password@localhost/testdb")
    monkeypatch.setenv("OPENAI_API_KEY", "test_api_key")
    monkeypatch.setenv("SECRET_KEY", "test_secret_key")

    config = Config()
    assert config.DATABASE_URL == "postgresql://user:password@localhost/testdb"
    assert config.OPENAI_API_KEY == "test_api_key"
    assert config.SECRET_KEY == "test_secret_key"