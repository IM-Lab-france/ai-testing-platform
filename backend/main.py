from fastapi import FastAPI
from src.db.session import engine, Base
from src.api.ai_providers import router as ai_providers_router
from src.api.campaigns import router as campaigns_router
from src.core.config import config
from src.core.logging import setup_logging

# Configuration du logging
setup_logging()

# Initialisation de l'application FastAPI
app = FastAPI()

# Création des tables de la base de données
Base.metadata.create_all(bind=engine)

# Inclusion des routes
app.include_router(ai_providers_router, prefix="/api", tags=["AI Providers"])
app.include_router(campaigns_router, prefix="/api", tags=["Campaigns"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Testing Platform"}

# Point d'entrée principal de l'application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)