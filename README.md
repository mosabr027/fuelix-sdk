# FuelIX SDK (Unofficial) by Rocket Science 🚀

This SDK provides a clean Python interface to the [FuelIX API](https://api-beta.fuelix.ai), including support for:

- Assistants (chat, threads, runs)
- Core features (chat completions, image generation)
- API key authentication

---

##  Installation

```bash
git clone https://github.com/mosabr027/fuelix-sdk.git
cd fuelix-sdk
pip install -e .
```

---

##  Authentication

You must provide your FuelIX API key manually:

```python
from fuelix_sdk import FuelixClient

client = FuelixClient(api_key="..-...your-key...")
```

---

##  Assistant Functions (to call other functions always get an assistant id with client.assistants.chat()

### List all assistants
```python
assistants = client.assistants.list()
print([a["name"] for a in assistants])
```

### Chat with assistant
```python
assistant_id = assistants[0]["id"]
reply = client.assistants.chat(assistant_id, "Explain quantum gravity")
print(reply)
```

---

##  Core Chat Completion (OpenAI style)

```python
messages = [{"role": "user", "content": "Tell me a joke"}]
response = client.core.chat_completion(
    model="claude-3-5-haiku",
    messages=messages,
    temperature=0.7,
    max_tokens=100
)
print(response["choices"][0]["message"]["content"])
```

---

## Generate an Image

```python
from fuelix_sdk.core.images import generate_image

image_data = generate_image(
    client,
    prompt="A robot cooking in a futuristic kitchen",
    model="imagen-3",
    size="512x512"
)

# Decode and display image
import base64
from PIL import Image
from io import BytesIO

img_bytes = base64.b64decode(image_data["b64_json"])
image = Image.open(BytesIO(img_bytes))
image.show()
```

---

## Thread + Run (Manual Usage)

```python
from fuelix_sdk.assistants.runs import create_thread_and_run
from fuelix_sdk.assistants.threads import get_latest_assistant_reply

result = create_thread_and_run(client, assistant_id, "What's the meaning of life?")
response = get_latest_assistant_reply(client, result["thread_id"])
print(response)
```

---

## Test Notebook

See [`examples/fuelix_demo_notebook.ipynb`](examples/fuelix_demo_notebook.ipynb) for a complete walk-through.

---

## SDK Structure

```
fuelix_sdk/
├── auth.py
├── client.py
├── config.py
├── core/
│   ├── chat.py
│   └── images.py
└── assistants/
    ├── assistant.py
    ├── threads.py
    └── runs.py
```

---

## 📫 Contributions

This is an unofficial community SDK — feel free to fork and improve!
