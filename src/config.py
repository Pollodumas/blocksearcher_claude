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

def check_anthropic_api_key():
    """Check and set Anthropic API key from Streamlit secrets"""
    if 'ANTHROPIC_API_KEY' in st.secrets:
        os.environ['ANTHROPIC_API_KEY'] = st.secrets['ANTHROPIC_API_KEY']
        return True
    st.error("Please set ANTHROPIC_API_KEY in your secrets")
    return False