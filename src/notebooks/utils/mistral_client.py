import json
import re
import fitz  # PyMuPDF
import requests
from typing import Optional
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "mistral"

def call_llm(system_prompt: str, user_message: str, temperature: float = 0.1) -> str:
    """
    Low temperature by default — we want structured extraction,
    not creative responses. Only the refinement agent uses higher temp.
    """
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message}
        ],
        "temperature": temperature,
        "stream": False
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
        return resp.json().get("message", {}).get("content", "").strip()
    except Exception as e:
        return f"LLM call failed: {e}"

def safe_json(raw: str) -> dict:
    """
    Strip markdown fences if LLM wraps response in ```json blocks.
    Then parse. Return empty dict on failure.
    """
    cleaned = re.sub(r"```json|```", "", raw).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        print(f"[WARN] Could not parse JSON:\n{cleaned[:300]}")
        return {}