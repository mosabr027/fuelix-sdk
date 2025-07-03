# images.py - Image generation endpoint

import requests

def generate_image(client, prompt, model="dall-e-3", size="512x512"):
    url = f"{client.base_url}/images/generations"
    payload = {
        "model": model,
        "prompt": prompt,
        "n": 1,
        "size": size
    }
    resp = requests.post(url, headers=client.headers, json=payload)
    resp.raise_for_status()
    return resp.json()["data"][0]
