# assistant.py - List assistants

import requests

def list_assistants(client):
    url = f"{client.base_url}/assistants"
    resp = requests.get(url, headers=client.headers)
    resp.raise_for_status()
    return resp.json().get("data", [])
