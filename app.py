import streamlit as st

#---Title and page links---#
#title
st.markdown("<h1 style='text-align: center; color: white;'>East London Council Comparison App</h1>", unsafe_allow_html=True)
st.markdown("Pages:")

st.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊")
st.page_link("pages/statistics_page.py", label="Contacting Your Council", icon="📱")

st.divider()


#---Introduction to the app and what it does---

#using markdown to make the text bigger and centered
st.title("Goal Of The App")
st.markdown("Councils in the UK are often felt to not represent their constituents very well. In a time where only 34% of people trust their local government, it is more important than ever to bring clarity.")
st.page_link("https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/bulletins/trustingovernmentuk/2023", label="ONS Survey on Trust in Government", icon="🔗")

