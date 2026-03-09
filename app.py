import streamlit as st
import pandas as pd
#streamlit_folium import folium_static does  maps
 
#streamlit tutorial: https://docs.streamlit.io/library/get-started/create-an-app

#title
st.title("hi")

#paragraphs
st.write("""
#
Hello *world!*
""")

#adding a sidebar with the options
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar")

#more sidebar things
st.sidebar.subheader("Subheader")
st.sidebar.write("This is the subheader")


#adding dataset to streamlit
#if wanted in the sidebar, add st.sidebar before the visual and error handling print
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith('.json'):
        df = pd.read_json(uploaded_file)
    st.success(f"File {uploaded_file.name} uploaded successfully!")
    st.dataframe(df)
else:
    st.error("No file uploaded")


#if the data is within the same directory as the app, you can read it directly without uploading
ready_df = pd.read_csv("my_data.csv")
st.dataframe(read_csv_dataset)


#df = pd.read_csv("my_data.csv")
#st.line_chart(df)