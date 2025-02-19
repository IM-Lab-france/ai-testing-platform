from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.campaign_service import CampaignService
from src.db.database import get_db

router = APIRouter()

@router.post("/campaigns/{campaign_id}/run")
async def run_campaign(campaign_id: int, db: Session = Depends(get_db)):
    """
    Lance une campagne spécifique.

    - **campaign_id**: L'identifiant de la campagne à lancer.
    - **db**: Session de base de données.

    Retourne un message de succès ou une erreur si la campagne n'a pas pu être lancée.
    """
    service = CampaignService(db, AIProviderService(db))
    try:
        await service.run_campaign(campaign_id)
        return {"message": "Campaign started successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))