import streamlit as st

# Title and Icon
# \U0001F304
st.set_page_config(page_title="PIE Text-to-Speech", page_icon='\U0001F5EF')
st.title('Proto-Indo-European Text to Speech')

# load the app code from app.py
from src.app.app import *