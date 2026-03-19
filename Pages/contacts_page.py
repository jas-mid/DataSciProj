import streamlit as st
import pandas as pd
from data_handling import load_and_clean_data

#---links to other pages---

#using columns to make the page links go next to eachother instead of on top of each other
col1, col2, col3 = st.columns(3)
#page links
col1.page_link("app.py", label="Home", icon="🏠")
col2.page_link("pages/statistics_page.py", label="Statistics Comparison Tool", icon="📊")
col3.page_link("pages/contacts_page.py", label="Contacting Your Council", icon="📱", disabled =True)
st.divider()

#---Load and clean the data---
data = load_and_clean_data("EDSP_employees_and_debt_data.csv")
#gaining boroughs
boroughs = sorted(
    [b for b in data["Borough"].unique() if b != "Greater London Average"]
)

#---Laying out varaibles for the page---
selected_borough = "placeholder"

#---Title and introduction to the page---
st.header("Getting Your Voice Heard")

#---Selecting your council in the sidebar---
st.sidebar.subheader("Select Your Council")
for borough in boroughs:
    if st.sidebar.button(borough):
        selected_borough = borough

#---Displaying the contact information for the selected council---

#function to display the contact information for the selected council
def display_contact_info(selected_borough):

    #displays the council name
    st.subheader(selected_borough + " Council")

    #initialising link to the website and determining what it will be based on the selected borough
    link=""
    if selected_borough == "Barking & Dagenham":
        link = "https://www.lbbd.gov.uk/contact-us/"
    elif selected_borough == "Hackney":
        link = "https://hackney.gov.uk/contact-us"
    elif selected_borough == "Havering":
        link = "https://www.havering.gov.uk/contactus"
    elif selected_borough == "Newham":
        link = "https://www.newham.gov.uk/contact-information"
    elif selected_borough == "Redbridge":
        link = "https://www.redbridge.gov.uk/contact-us/"
    elif selected_borough == "Tower Hamlets":
        link = "https://www.towerhamlets.gov.uk/content_pages/contact_us/contact-us.aspx"
    elif selected_borough == "Waltham Forest":
        link = "https://www.walthamforest.gov.uk/contact-us"
    

    st.page_link(link, label="Contact " + selected_borough + " Contact Us Page", icon="📱")

#Page logic to display the contact information or a message initially
if selected_borough == "placeholder":
    st.warning("Select your council to see how you can get your opinion to them")
else:
    display_contact_info(selected_borough)