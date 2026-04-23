import os
import streamlit as st

os.environ["TOKENIZERS_PARALLELISM"] = "false"


def get_openai_api_key() -> str:
    return st.secrets["general"]["openai_api_key"]