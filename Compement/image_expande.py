import streamlit as st
def expand_done(data,file):
 cols1,cols2=st.columns(2)
 if 'result_url' in data :
  with cols1:
   st.image(data['result_url'],width=300,caption="Expanded Image")
   st.link_button("Download", data['result_url'] )
  with cols2:
   
   st.image(file,width=300,caption="Original Image")
