import requests
import streamlit as st
from Compement.page import Chatbot
from Ai.Generate_image import Generate_image
from Compement.result import result
from Compement.UploadImage import UploadImage
from  Ai.generate_background import generate_background
from Compement.backgroundchange import change
from Ai.expand import expand
from Compement.expand_upload import upload_image
from Compement.image_expande import expand_done

def main():
 st.title(" AI studio")
 st.markdown(
    " :orange-badge[⚠️ English is required] "
)
  
 tab1, tab2, tab3 = st.tabs(["Generate Image ", "Expand image", "Generate Background"])
 with tab1:
 
  prompt=Chatbot()
  response=Generate_image(prompt)
  result(response,prompt)
 with tab2:
    file,url=upload_image()
    expanded=expand(file,url)
    expand_done(expanded,file)
 with tab3:
   Image,prompte= UploadImage()
   data=generate_background(Image,prompte)
   change(data,prompte)




main()


