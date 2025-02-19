from sqlalchemy.orm import Session
from src.db.models import Campaign, Question, CampaignResult, AIProvider
from src.services.ai_service import AIProviderService

class CampaignService:
    def __init__(self, db_session: Session, ai_service: AIProviderService):
        self.db_session = db_session
        self.ai_service = ai_service

    async def get_campaign_questions(self, campaign_id: int):
        """
        Récupère les questions associées à une campagne.

        - **campaign_id**: L'identifiant de la campagne.

        Retourne une liste de questions.
        """
        campaign = await self.db_session.get(Campaign, campaign_id)
        if not campaign:
            raise ValueError(f"Campaign {campaign_id} not found")

        questions = await self.db_session.query(Question).filter(Question.id.in_(campaign.questions)).all()
        return questions

    async def run_campaign(self, campaign_id: int):
        """
        Lance une campagne spécifique.

        - **campaign_id**: L'identifiant de la campagne à lancer.

        Enregistre les résultats de la campagne dans la base de données.
        """
        campaign = await self.db_session.get(Campaign, campaign_id)
        if not campaign:
            raise ValueError(f"Campaign {campaign_id} not found")

        questions = await self.get_campaign_questions(campaign_id)

        for question in questions:
            for provider_id in campaign.config['providers']:
                try:
                    provider = await self.ai_service.get_provider(provider_id)
                    result = await provider.generate_response(question.content)

                    # Enregistrement du résultat
                    campaign_result = CampaignResult(
                        campaign_id=campaign_id,
                        question_id=question.id,
                        ai_provider_id=provider_id,
                        response=result['response'],
                        tokens_count=result['tokens'],
                        response_time=result['time']
                    )
                    self.db_session.add(campaign_result)
                except Exception as e:
                    # Gestion des erreurs
                    campaign_result = CampaignResult(
                        campaign_id=campaign_id,
                        question_id=question.id,
                        ai_provider_id=provider_id,
                        error=str(e)
                    )
                    self.db_session.add(campaign_result)

        await self.db_session.commit()