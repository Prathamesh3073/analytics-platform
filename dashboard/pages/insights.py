import streamlit as st
from utils.helper import load_data

st.title("🧠 Insights")

df = load_data("data/sales.csv")

if not df.empty:
    best_product = df.groupby("Product")["Sales"].sum().idxmax()
    worst_region = df.groupby("Region")["Sales"].sum().idxmin()

    st.success(f"🔥 Best Product: {best_product}")
    st.warning(f"⚠️ Worst Region: {worst_region}")