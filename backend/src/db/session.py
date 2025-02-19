from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from src.core.config import config

# Création de l'engine de la base de données
engine = create_engine(config.DATABASE_URL, pool_pre_ping=True)

# Création de la base de données déclarative
Base = declarative_base()

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """
    Obtient une nouvelle session de base de données.

    Retourne une nouvelle instance de session.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()