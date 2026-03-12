import streamlit as st

#---links to other pages---

#using columns to make the page links go next to eachother instead of on top of each other
col1, col2, col3 = st.columns(3)
#page links
col1.page_link("app.py", label="Home", icon="🏠")
col2.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊")
col3.page_link("pages/contacts_page.py", label="Contacting Your Council", icon="📱", disabled =True)
st.divider()