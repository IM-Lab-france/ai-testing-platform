import csv
from typing import List, Dict, Any
from src.db.schemas import AIProvider, Question, Campaign, CampaignResult

def write_csv(file_path: str, data: List[Dict[str, Any]], headers: List[str]):
    """
    Écrit des données dans un fichier CSV.

    - **file_path**: Le chemin du fichier CSV à écrire.
    - **data**: Les données à écrire sous forme de liste de dictionnaires.
    - **headers**: Les en-têtes du fichier CSV.
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Lit des données depuis un fichier CSV.

    - **file_path**: Le chemin du fichier CSV à lire.

    Retourne les données sous forme de liste de dictionnaires.
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def export_ai_providers_to_csv(file_path: str, ai_providers: List[AIProvider]):
    """
    Exporte les fournisseurs d'IA vers un fichier CSV.

    - **file_path**: Le chemin du fichier CSV à écrire.
    - **ai_providers**: La liste des fournisseurs d'IA à exporter.
    """
    headers = ["id", "name", "description", "api_url", "module_path", "class_name", "is_active", "created_at", "updated_at"]
    data = [provider.dict() for provider in ai_providers]
    write_csv(file_path, data, headers)

def export_questions_to_csv(file_path: str, questions: List[Question]):
    """
    Exporte les questions vers un fichier CSV.

    - **file_path**: Le chemin du fichier CSV à écrire.
    - **questions**: La liste des questions à exporter.
    """
    headers = ["id", "content", "category", "tags", "created_at", "updated_at"]
    data = [question.dict() for question in questions]
    write_csv(file_path, data, headers)

def export_campaigns_to_csv(file_path: str, campaigns: List[Campaign]):
    """
    Exporte les campagnes vers un fichier CSV.

    - **file_path**: Le chemin du fichier CSV à écrire.
    - **campaigns**: La liste des campagnes à exporter.
    """
    headers = ["id", "name", "description", "status", "config", "created_at", "started_at", "completed_at"]
    data = [campaign.dict() for campaign in campaigns]
    write_csv(file_path, data, headers)

def export_campaign_results_to_csv(file_path: str, results: List[CampaignResult]):
    """
    Exporte les résultats des campagnes vers un fichier CSV.

    - **file_path**: Le chemin du fichier CSV à écrire.
    - **results**: La liste des résultats des campagnes à exporter.
    """
    headers = ["id", "campaign_id", "question_id", "ai_provider_id", "response", "tokens_count", "response_time", "error", "created_at"]
    data = [result.dict() for result in results]
    write_csv(file_path, data, headers)