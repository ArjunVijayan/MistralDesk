import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "mistral"  # or "mistral"



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

if __name__ == "__main__":
    SYSTEM_PROMPT = """You are a helpful assistant for software developers. You can answer questions about programming, algorithms, data structures, and software design. You can also provide code snippets and explanations to help developers solve their problems."""
    
    while True:
        user_input = input("Ask a question (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        answer = ask_llm(user_input)
        print("Answer:", answer)