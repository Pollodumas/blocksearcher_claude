import os
import streamlit as st

def init_page():
    """Initialize Streamlit page configuration"""
    st.set_page_config(
        page_title="Blockchain Research AI",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("🔗 Blockchain Research AI")

def check_api_key():
    """Check and set OpenAI API key from Streamlit secrets"""
    if 'OPENAI_API_KEY' in st.secrets:
        os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
        return True
    st.error("Please set OPENAI_API_KEY in your secrets")
    return False