from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class AIProvider(Base):
    __tablename__ = "ai_providers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    api_url = Column(String)
    module_path = Column(String)  # Chemin vers le module Python
    class_name = Column(String)  # Nom de la classe à instancier
    api_key = Column(String)  # Stocké de manière cryptée
    config = Column(JSON)  # Configuration spécifique à l'IA
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    category = Column(String)
    tags = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, nullable=False)  # pending, running, completed, failed
    config = Column(JSON)  # Configuration spécifique de la campagne
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    results = relationship("CampaignResult", back_populates="campaign")

class CampaignResult(Base):
    __tablename__ = "campaign_results"

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    ai_provider_id = Column(Integer, ForeignKey("ai_providers.id"))
    response = Column(String)
    tokens_count = Column(Integer)
    response_time = Column(Float)
    error = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    campaign = relationship("Campaign", back_populates="results")
    question = relationship("Question")
    ai_provider = relationship("AIProvider")