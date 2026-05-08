import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "mistral"  # or "mistral"


def get_text_response(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 300,
            "stream": False,
        }
    )

    with open("response.json", "w") as f:
        f.write(response.text)

    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")

def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 300,
            "stream": False,
        }
    )

    return response.json()

def ask_llm_stream(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 300,
            "stream": True,
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            yield line.decode("utf-8")

if __name__ == "__main__":
    SYSTEM_PROMPT = """You are a helpful assistant for software developers. You can answer questions about programming, algorithms, data structures, and software design. You can also provide code snippets and explanations to help developers solve their problems."""
    
    while True:
        user_input = input("Ask a question (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        answer = get_text_response(user_input)
        print("Answer:", answer)