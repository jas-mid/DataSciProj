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
st.markdown("This page allows you to compare the statistics of different measures that Boroughs in East London have direct control over")

#---Load and clean the data---
data = load_and_clean_data("EDSP_council_performance_data.csv")

#---Select Boroughs to compare---
st.sidebar.subheader("Select Boroughs to Compare:")
boroughs = sorted(
    [b for b in data["Borough"].unique() if b != "Greater London Average"]
)
selected_boroughs = ["Greater London Average"]  # Always include Greater London Average for comparison
for borough in boroughs:
    if st.sidebar.checkbox(borough):
        selected_boroughs.append(borough)



#---Select which metrics you want to see---
metrics = data.columns[1:]  #as the first column is 'Borough'
selected_metrics = st.selectbox("Select Metrics to Compare", metrics)

#---Filter the data based on user selections---
plot_data = data[data["Borough"].isin(selected_boroughs)]

if selected_metrics=="Debt In Gbp":
    st.warning("There is no wide data for the Greater London Average for this metric, so it is not included in the graph.")
elif selected_metrics =="Number Of Employees":
    st.warning("There is no wide data for the Greater London Average for this metric, so it is not included in the graph.")

if selected_metrics:

    metric = selected_metrics

    fig = px.bar(
        plot_data,
        x="Borough",
        y=metric,
        color="Borough",
        title=f"{metric} Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Select what data you want to display.")

if selected_metrics == "Debt in GBP":
    st.warning("There is no wide data for the Greater London Average for this metric, so it is not included in the graph.")