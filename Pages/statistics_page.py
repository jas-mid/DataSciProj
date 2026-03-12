import streamlit as st
import plotly.express as px
import pandas as pd
from data_handling import load_and_clean_data

#---links to other pages---

#using columns to make the page links go next to eachother instead of on top of each other
col1, col2, col3 = st.columns(3)
#page links
col1.page_link("app.py", label="Home", icon="🏠")
col2.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊",disabled=True)
col3.page_link("pages/contacts_page.py", label="Contacting Your Borough", icon="📱")
st.divider()

#---Title and introduction to the page---
st.header("Statistics Comparison Tool")
st.markdown("This page allows you to compare the statistics of different Boroughs in East London")

#---Load and clean the data---
data = load_and_clean_data("EDSP_council_performance_data.csv")

#---Select Boroughs to compare---
boroughs = data[data["Borough"] != "Greater London Average"]["Borough"].unique()
selected_boroughs = st.sidebar.multiselect("Select Boroughs to Compare", options=boroughs, default=boroughs[:0])

#---Select which metrics you want to see---
metrics = data.columns[1:]  #as the first column is 'Borough'
selected_metrics = st.multiselect("Select Metrics to Compare", options=metrics, default=metrics[:0])
