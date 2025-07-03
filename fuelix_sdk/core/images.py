# images.py - Image generation endpoint

import requests

def generate_image(client, prompt, model, size):
    """
    Generate an image using the FuelIX API.

    Parameters:
    - client: FuelixClient instance
    - prompt (str): Text prompt describing the image to generate
    - model (str): The model to use (e.g., "dall-e-3")
    - size (str): Image size (e.g., "512x512", "1024x1024")

    Returns:
    - dict: The first image object from the API response
    """
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
