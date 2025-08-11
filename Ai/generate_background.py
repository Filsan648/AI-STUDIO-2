import requests
import base64
def generate_background (Image,prompte):
 url = "https://engine.prod.bria-api.com/v1/background/replace"

 payload = {
  "bg_prompt":prompte,
  "num_results": 2,
  "sync": True,
  "image_url":Image
 }

 headers = {
  "Content-Type": "application/json",
  "api_token": " ",
 }

 response = requests.post(url, json=payload, headers=headers)
 data = response.json()
 return(data)