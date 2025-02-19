import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.models import Base, AIProvider, Question, Campaign, CampaignResult

# Configuration de la base de données de test
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Création des tables dans la base de données de test
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_ai_provider_model(db_session):
    provider = AIProvider(name="TestProvider", api_url="http://test.com")
    db_session.add(provider)
    db_session.commit()
    assert provider.id is not None

def test_question_model(db_session):
    question = Question(content="Test question")
    db_session.add(question)
    db_session.commit()
    assert question.id is not None

def test_campaign_model(db_session):
    campaign = Campaign(name="Test Campaign", status="pending")
    db_session.add(campaign)
    db_session.commit()
    assert campaign.id is not None

def test_campaign_result_model(db_session):
    provider = AIProvider(name="TestProvider", api_url="http://test.com")
    question = Question(content="Test question")
    campaign = Campaign(name="Test Campaign", status="pending")
    db_session.add(provider)
    db_session.add(question)
    db_session.add(campaign)
    db_session.commit()

    result = CampaignResult(
        campaign_id=campaign.id,
        question_id=question.id,
        ai_provider_id=provider.id,
        response="Test response"
    )
    db_session.add(result)
    db_session.commit()
    assert result.id is not None