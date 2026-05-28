import requests
from typing import Any

# Local Ollama chat endpoint and model
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "mistral"

SYSTEM_PROMPT = (
    "You are a helpful assistant for general quesions. You cangree or N=answer others quesions"
)

def ask_mistral(prompt: str) -> str:
    """Send a chat request to the local Ollama server and return the assistant text."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 300,
        "stream": False,
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
    except requests.RequestException as e:
        return f"Request failed: {e}"

    try:
        data = resp.json()
    except ValueError:
        return resp.text

    return data.get("message", {}).get("content", "").strip()
