import logging
import os
import tempfile
from src.core.logging import setup_logging

def test_logging_configuration():
    # Crée un fichier temporaire pour les logs
    with tempfile.NamedTemporaryFile(delete=False) as temp_log_file:
        temp_log_file_name = temp_log_file.name

    # Configure le logging pour utiliser le fichier temporaire
    os.environ["LOG_FILE"] = temp_log_file_name
    os.environ["LOG_LEVEL"] = "DEBUG"
    setup_logging()

    logger = logging.getLogger(__name__)

    # Envoie des messages de log à différents niveaux
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    # Vérifie que les messages sont enregistrés dans le fichier de log
    with open(temp_log_file_name, 'r') as log_file:
        logs = log_file.read()
        assert "debug message" in logs
        assert "info message" in logs
        assert "warning message" in logs
        assert "error message" in logs
        assert "critical message" in logs

    # Nettoie le fichier temporaire
    os.remove(temp_log_file_name)