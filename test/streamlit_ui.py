import sys
from pathlib import Path

import streamlit as st

# Add src directory to import path so we can import the local llm helper.
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from services.llm import get_text_response

st.set_page_config(page_title="Mistral Chatbot", layout="wide")

st.title("Mistral Chatbot")
st.write("Talk to your local Mistral model via Ollama.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Settings")
    st.write("Ensure `ollama serve` is running and the Mistral model is loaded.")
    st.markdown("- Host: `http://127.0.0.1:11434`")
    st.markdown("- Model: `mistral`")
    if st.button("Clear chat"):
        st.session_state.chat_history = []

prompt = st.chat_input("Ask Mistral a question...")
if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.spinner("Waiting for response..."):
        assistant_text = get_text_response(prompt)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_text})

for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
