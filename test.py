import requests

url = f"http://127.0.0.1:8000"
print(url)

response = requests.get(url)
print(response.content)
