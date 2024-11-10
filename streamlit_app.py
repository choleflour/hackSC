import streamlit as st
import requests

st.title("Flask + Streamlit App")

if st.button("Get Data from Flask"):
    response = requests.get("http://localhost:5000/get_data")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.write("Error connecting to Flask")
