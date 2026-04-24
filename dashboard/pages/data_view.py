import streamlit as st
from utils.helper import load_data

st.title("📄 Data Viewer")

df = load_data("data/sales.csv")

st.dataframe(df)