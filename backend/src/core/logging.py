import logging
import os

def setup_logging():
    """
    Configure le système de logging pour l'application.

    Les logs sont enregistrés dans un fichier et affichés dans la console.
    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_file = os.getenv("LOG_FILE", "app.log")

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    # Supprime les handlers existants pour éviter les doublons
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []

# Configuration initiale du logging
setup_logging()

# Exemple d'utilisation
logger = logging.getLogger(__name__)