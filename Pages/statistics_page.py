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
col3.page_link("pages/contacts_page.py", label="Contacting Your Council", icon="📱")
st.divider()

#---Title and introduction to the page---
st.header("Statistics Comparison Tool")
st.markdown("This page allows you to compare the statistics of different councils in East London")
