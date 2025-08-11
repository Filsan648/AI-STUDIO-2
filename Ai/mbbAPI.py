import streamlit as st
import requests
def mbb(uploaded_file):
     api_key = ""
     url = "https://api.imgbb.com/1/upload"
     payload = {
                  "key":"api_key",
                "image": uploaded_file.getvalue()
                }
     response = requests.post(url, files={"image": uploaded_file.getvalue()}, data={"key": api_key})
     file_url = response.json()["data"]["url"]
     return( file_url)