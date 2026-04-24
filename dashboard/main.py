import sys
import os

# Fix import path (IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helper import load_data

st.set_page_config(layout="wide")

# ---------------- HEADER ---------------- #
st.title("📊 Business Analytics Dashboard")

# ---------------- LOAD DATA ---------------- #
try:
    df = load_data("data/sales.csv")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ---------------- KPI ---------------- #
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

total_sales = int(df["Sales"].sum())
total_profit = int(df["Profit"].sum())
avg_sales = int(df["Sales"].mean())

col1.metric("💰 Total Sales", total_sales)
col2.metric("💸 Total Profit", total_profit)
col3.metric("📈 Avg Sales", avg_sales)

# ---------------- FILTERS ---------------- #
st.sidebar.header("🔍 Filters")

product_filter = st.sidebar.multiselect("Product", df["Product"].unique())
region_filter = st.sidebar.multiselect("Region", df["Region"].unique())

if product_filter:
    df = df[df["Product"].isin(product_filter)]

if region_filter:
    df = df[df["Region"].isin(region_filter)]

# ---------------- CHARTS ---------------- #
st.subheader("📦 Sales by Product")

product_data = df.groupby("Product", as_index=False)["Sales"].sum()

fig1 = px.bar(product_data, x="Product", y="Sales", color="Product")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🌍 Sales by Region")

region_data = df.groupby("Region", as_index=False)["Sales"].sum()

fig2 = px.pie(region_data, names="Region", values="Sales")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 Sales Trend")

trend_data = df.groupby("Date", as_index=False)["Sales"].sum()

fig3 = px.line(trend_data, x="Date", y="Sales", markers=True)
st.plotly_chart(fig3, use_container_width=True)

# ---------------- INSIGHTS ---------------- #
st.subheader("🧠 Insights")

if not df.empty:
    best_product = df.groupby("Product")["Sales"].sum().idxmax()
    worst_region = df.groupby("Region")["Sales"].sum().idxmin()

    st.success(f"🔥 Best Product: {best_product}")
    st.warning(f"⚠️ Lowest Region: {worst_region}")

# ---------------- DATA TABLE ---------------- #
st.subheader("📄 Data Preview")
st.dataframe(df)

# ---------------- DOWNLOAD ---------------- #
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Data",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)
