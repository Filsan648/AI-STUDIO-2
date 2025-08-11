import requests
import streamlit as st
def result(response,prompt):
 data=response.json()

 if prompt:
 
  for i in data['result']:
  
    if i['urls']:
     st.image(i['urls'],width=500)
     for j in i['urls']:
       response = requests.get(j )
       st.link_button("Download",  j )
 else:
  st.caption("Generate your image with your imagination")
  
