import os
import streamlit as st

os.environ["TOKENIZERS_PARALLELISM"] = "false"


def get_openai_api_key() -> str:
    env_key = os.environ.get("OPENAI_API_KEY")
    if env_key:
        return env_key

    try:
        return st.secrets["general"]["openai_api_key"]
    except (KeyError, FileNotFoundError):
        st.error(
            "OpenAI API key not found. Set the OPENAI_API_KEY environment "
            "variable, or add it to .streamlit/secrets.toml under "
            '[general] as openai_api_key = "sk-...".'
        )
        st.stop()
