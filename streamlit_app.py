import streamlit as st
import requests

st.title("Flask + Streamlit App")

if st.button("Get Data from Flask"):
    response = requests.get("http://127.0.0.1:5000/")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.write("Error connecting to Flask")


def list_trails(response):
    trails = response.json()['businesses']
    for k, v in trails.items():
        st.header(v)
        