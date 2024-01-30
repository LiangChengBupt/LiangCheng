import requests

url = "http://localhost:8283/api/models"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)