import requests
import streamlit as st
from Compement.page import Chatbot
import time
def Generate_image(prompt):

 model_version="2.3"
 api_overview="https://engine.prod.bria-api.com/v1"
 url="https://engine.prod.bria-api.com/v1/text-to-image/base/"+model_version

 payload={
    "prompt":prompt,
    "sync":True
 }

 header={
    "content-type":"application/json",
    "api_token":"dcb510d623b84758aa83414d754b5860",

 }

 response=requests.post(url,json=payload,headers=header)
 return response