import streamlit as st
import plotly.express as px
from dashboard.utils.helper import load_data, get_kpis

st.set_page_config(layout="wide")

st.title("📊 Business Dashboard")

# Upload
uploaded_file = st.sidebar.file_uploader("Upload CSV")

if uploaded_file:
    df = load_data(uploaded_file)
else:
    df = load_data("data/sales.csv")

# KPIs
kpis = get_kpis(df)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Sales", kpis["total_sales"])
col2.metric("💸 Profit", kpis["total_profit"])
col3.metric("📈 Avg Sales", kpis["avg_sales"])

# Chart
st.subheader("Sales by Product")

product_data = df.groupby("Product", as_index=False)["Sales"].sum()

fig = px.bar(product_data, x="Product", y="Sales", color="Product")
st.plotly_chart(fig, use_container_width=True)