import streamlit as st

#---Title and page links---#
#title
st.title("Welcome to the East London Council Rating App")

st.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊")
st.page_link("pages/statistics_page.py", label="Contacting Your Council", icon="📱")

st.divider()


#---Introduction to the app and what it does---#
st.header("Goal of the App")

