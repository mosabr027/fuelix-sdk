# FuelIX Python SDK

## Installation

```bash
git clone <your_repo_url>
cd fuelix_sdk_package
pip install -e .
```

## Authentication

Set your FuelIX API key:

```bash
export FUELIX_API_KEY=sk-...
```
Or input it interactively when prompted.

## Example Usage

```python
from fuelix_sdk import FuelixClient

client = FuelixClient(api_key="sk-...")
assistants = client.assistants.list()
response = client.assistants.chat(assistants[0]['id'], "What is AI?")
print(response)
```
