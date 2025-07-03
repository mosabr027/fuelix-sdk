# threads.py - Fetch assistant reply from thread messages

import requests

def get_latest_assistant_reply(client, thread_id):
    url = f"{client.base_url}/threads/{thread_id}/messages"
    resp = requests.get(url, headers=client.headers)
    resp.raise_for_status()
    messages = resp.json().get("data", [])
    for msg in messages:
        if msg.get("role") == "assistant":
            for block in msg.get("content", []):
                if block.get("type") == "text":
                    return block["text"]["value"]
    return "[No assistant response]"
