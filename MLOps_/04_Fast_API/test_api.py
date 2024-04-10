import requests

url = "http://127.0.0.1:8000/predict"

files = {'img': open('imgs/1.png', 'rb')}
response = requests.post(url, files=files)
print(response.json())