import pytest
from sqlalchemy.orm import Session
from src.db.session import get_db, SessionLocal, engine, Base
from src.core.config import config

# Configuration de la base de données de test
DATABASE_URL = "sqlite:///:memory:"
config.DATABASE_URL = DATABASE_URL

# Création des tables dans la base de données de test
Base.metadata.create_all(bind=engine)

def test_get_db():
    # Vérifie que la fonction get_db retourne une instance de Session
    with get_db() as db:
        assert isinstance(db, Session)

def test_session_commit():
    # Vérifie que la session peut commiter une transaction
    with get_db() as db:
        # Exemple de commit (aucune table n'est nécessaire pour ce test)
        db.commit()

def test_session_rollback():
    # Vérifie que la session peut effectuer un rollback
    with get_db() as db:
        try:
            # Forcer une exception pour tester le rollback
            raise ValueError("Test rollback")
        except Exception:
            # Vérifie que la session est rollbackée en cas d'erreur
            assert db.closed