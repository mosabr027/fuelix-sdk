# runs.py - Create thread + run

import requests

def create_thread_and_run(client, assistant_id, prompt):
    url = f"{client.base_url}/threads/runs"
    payload = {
        "assistant_id": assistant_id,
        "thread": {
            "messages": [{"role": "user", "content": prompt}]
        }
    }
    resp = requests.post(url, headers=client.headers, json=payload)
    resp.raise_for_status()
    return resp.json()
