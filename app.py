import streamlit as st

#---Title and page links---#
#title
st.title("Welcome to the East London Council Rating App")

st.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊")
st.page_link("pages/statistics_page.py", label="Contacting Your Council", icon="📱")

st.divider()


#---Introduction to the app and what it does---

#using markdown to make the text bigger and centered
st.markdown("<h1 style='text-align: center; color: white;'>Goal of the App</h1>", unsafe_allow_html=True)


