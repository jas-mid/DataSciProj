import streamlit as st

#---links to other pages---
st.page_link("app.py", label="Statistics Comparison Tool", icon="🏠")
st.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊", disabled =True)
st.page_link("pages/contacts_page.py", label="Contacting Your Council", icon="📱")