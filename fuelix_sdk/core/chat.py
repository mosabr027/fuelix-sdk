# chat.py - Handles /chat/completions

import requests

class CoreModule:
    def __init__(self, client):
        self.client = client

    def chat_completion(self, model, messages, temperature, max_tokens):
        """
        Send a chat completion request to the FuelIX API.

        Parameters:
        - model (str): The model to use (e.g. "gpt-3.5-turbo")
        - messages (list): List of dicts like [{"role": "user", "content": "Hello"}]
        - temperature (float): Sampling temperature (e.g. 0.7)
        - max_tokens (int): Max number of tokens to generate in the response

        Returns:
        - dict: JSON response from the API
        """
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
