# MistralDesk

`MistralDesk` is a local development assistant that uses Ollama and Mistral to provide an offline chatbot interface for software developers.

It includes:
 - a local `llm` helper for calling Ollama's chat API,
 - a Streamlit-based chatbot UI in `test/streamlit_ui.py`,
 - support for local model inference with Mistral via Ollama.

## Run locally
1. Start Ollama: `ollama serve`
2. Run the Streamlit app: `streamlit run test/streamlit_ui.py`

## Notes
- Use a Python virtual environment.
- Install dependencies like `streamlit` and `requests` before running.
