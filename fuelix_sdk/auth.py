# auth.py - Handles API key input and headers

def get_api_key():
    import os
    key = os.getenv("FUELIX_API_KEY")
    if not key:
        key = input("Enter your FuelIX API key: ").strip()
    return key

def get_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
