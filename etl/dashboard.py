"""
Dashboard interattiva stile Power BI: mappa e aggregati stock movement
Lancia con: streamlit run etl/dashboard.py
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Amazon DW Dashboard", layout="wide")
st.title("Amazon Data Warehouse - Stock Movement Dashboard")

# Percorsi
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
proc_dir = os.path.join(base_dir, "data", "processed")

# Carica dati
location = pd.read_parquet(os.path.join(proc_dir, "location"))
fact = pd.read_parquet(os.path.join(proc_dir, "inventory"))

# Join per country/region
fact_loc = fact.merge(location, left_on="WarehouseID", right_on="LocationID", how="left")

# Aggregati
agg_country = fact_loc.groupby("Country").agg({"Stock_Movement": "sum"}).reset_index()
agg_region = fact_loc.groupby("Region").agg({"Stock_Movement": "sum"}).reset_index()

# Mappa (usa lat/lon se disponibili, qui solo country)
fig_map = px.choropleth(
    agg_country,
    locations="Country",
    locationmode="country names",
    color="Stock_Movement",
    color_continuous_scale="Blues",
    title="Totale Stock Movement per Paese"
)

# Grafico barre region
fig_region = px.bar(
    agg_region.sort_values("Stock_Movement", ascending=False),
    x="Region", y="Stock_Movement",
    title="Totale Stock Movement per Regione",
    color="Stock_Movement",
    color_continuous_scale="Blues"
)

# Layout stile Power BI
col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(fig_map, use_container_width=True)
with col2:
    st.plotly_chart(fig_region, use_container_width=True)

st.markdown("---")
st.write("Dati aggregati e visualizzati in stile Power BI, generati da pipeline Spark ETL.")
