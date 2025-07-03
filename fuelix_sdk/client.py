# client.py - Main FuelixClient class

from fuelix_sdk.core import chat, images
from fuelix_sdk.assistants import assistant, threads, runs

class FuelixClient:
    def __init__(self, api_key: str):
        from fuelix_sdk import auth
        from fuelix_sdk.config import BASE_URL

        self.api_key = api_key
        self.headers = auth.get_headers(api_key)
        self.base_url = BASE_URL

        self.core = chat.CoreModule(self)
        self.assistants = AssistantModule(self)

class AssistantModule:
    def __init__(self, client):
        self.client = client

    def list(self):
        return assistant.list_assistants(self.client)

    def chat(self, assistant_id: str, prompt: str):
        run_data = runs.create_thread_and_run(self.client, assistant_id, prompt)
        return threads.get_latest_assistant_reply(self.client, run_data["thread_id"])
