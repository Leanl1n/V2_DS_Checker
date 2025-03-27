# settings.py

import os
from dotenv import load_dotenv
import streamlit as st

def load_settings():
    """Load settings from Streamlit secrets."""
    return {
        'DEEPSEEK_API_KEY': st.secrets.DEEPSEEK_API_KEY,
        'DEEPSEEK_USER': st.secrets.DEEPSEEK_USER,
        'DEEPSEEK_PASS': st.secrets.DEEPSEEK_PASS
    }

# Configuration settings
class Settings:
    API_KEY = os.getenv('DEEPSEEK_API_KEY')
    USER = os.getenv('DEEPSEEK_USER')
    PASSWORD = os.getenv('DEEPSEEK_PASS')
    API_URL = "https://api.deepseek.com/v1/chat/completions"