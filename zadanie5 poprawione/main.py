import requests

response = requests.get("https://randomfox.ca/floof")
fox = response.json()
print(fox['image'])
print(fox['link'])