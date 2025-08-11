import streamlit as st
def change(data,prompte):
  st.subheader(f"Background generated for the prompt: {prompte}")
  cols= st.columns(2)
  j=0
 
  if prompte !="":
   for i in data['result']:
    with cols[j]:
     st.image(i[0],width=300, caption=j)
     st.link_button("Download",  i[0] )
    
     j+=1
