import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def get_kpis(df):
    return {
        "total_sales": int(df["Sales"].sum()),
        "total_profit": int(df["Profit"].sum()),
        "avg_sales": int(df["Sales"].mean()) if not df.empty else 0
    }