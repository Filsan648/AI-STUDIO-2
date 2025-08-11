import streamlit as st
from Ai.mbbAPI import mbb
def upload_image():
 st.caption("Expand an image to fit different aspect ratios by generating new content to seamlessly fill the extended areas.")
 col1, col2 = st.columns(2)
 key_suffix=""
 if "file" not in st.session_state:
        st.session_state.file = None
 if "file_url" not in st.session_state:
        st.session_state.file_url = None   
 if "ratio" not in st.session_state:
        st.session_state.ratio = None   
 with col1:
  st.session_state.file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"], key=f"image_uploader_{key_suffix}")
 with col2:
   st.session_state.ratio=st.radio("Aspect ratio",("1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9"),horizontal=True) 
 if st.session_state.file is not None:
  st.session_state.file_url=mbb(st.session_state.file)
 return( st.session_state.file_url,st.session_state.ratio)