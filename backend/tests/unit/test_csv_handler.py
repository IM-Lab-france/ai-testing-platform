import os
import tempfile
from src.utils.csv_handler import write_csv, read_csv, export_ai_providers_to_csv
from src.db.schemas import AIProvider

def test_write_and_read_csv():
    headers = ["name", "value"]
    data = [{"name": "Item1", "value": 10}, {"name": "Item2", "value": 20}]

    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8') as temp_file:
        file_path = temp_file.name

    write_csv(file_path, data, headers)

    read_data = read_csv(file_path)
    assert len(read_data) == 2
    assert read_data[0]["name"] == "Item1"
    assert read_data[1]["value"] == "20"

    os.remove(file_path)

def test_export_ai_providers_to_csv():
    ai_providers = [
        AIProvider(id=1, name="Provider1", api_url="http://provider1.com"),
        AIProvider(id=2, name="Provider2", api_url="http://provider2.com")
    ]

    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8') as temp_file:
        file_path = temp_file.name

    export_ai_providers_to_csv(file_path, ai_providers)

    read_data = read_csv(file_path)
    assert len(read_data) == 2
    assert read_data[0]["name"] == "Provider1"
    assert read_data[1]["api_url"] == "http://provider2.com"

    os.remove(file_path)