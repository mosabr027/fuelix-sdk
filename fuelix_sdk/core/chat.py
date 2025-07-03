# chat.py - Handles /chat/completions

import requests

class CoreModule:
    def __init__(self, client):
        self.client = client

    def chat_completion(self, model, messages, temperature=0.7, max_tokens=300):
        url = f"{self.client.base_url}/chat/completions"
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        resp = requests.post(url, headers=self.client.headers, json=payload)
        resp.raise_for_status()
        return resp.json()
