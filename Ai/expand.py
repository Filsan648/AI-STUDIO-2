import requests

def expand(file_url,ratio):
 url = "https://engine.prod.bria-api.com/v1/image_expansion"

 payload = {
  "image_url": file_url,
  "aspect_ratio":ratio
 }

 headers = {
  "Content-Type": "application/json",
  "api_token":" ",
}

 response = requests.post(url, json=payload, headers=headers)

 data = response.json()

 return(data)