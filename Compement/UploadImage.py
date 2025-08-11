import streamlit as st
import base64
import requests
from Ai.mbbAPI import mbb
def UploadImage():
    st.caption("Generate a new background for an image while preserving the original subject.")
    if "bytes_data" not in st.session_state:
        st.session_state.bytes_data = None
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""
    if "file_url" not in st.session_state:
        st.session_state.file_url = ""  

    col1, col2 = st.columns(2)

    if st.session_state.bytes_data is None:
        uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
        
        if uploaded_file is not None:
            st.session_state.bytes_data = uploaded_file.read()
     
            st.session_state.file_url = mbb(uploaded_file)
            

    if st.session_state.bytes_data:
        with col1:
            st.image(st.session_state.bytes_data, width=500)
        with col2:
            st.session_state.prompt = st.text_input(
                "Describe the background", 
                value=st.session_state.prompt
            )

    return st.session_state.file_url, st.session_state.prompt
