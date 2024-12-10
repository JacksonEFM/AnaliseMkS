import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)
def upload():
    uploaded_file = st.file_uploader("Faça o upload da planilha Excel", type=["xlsx"])
    return uploaded_file