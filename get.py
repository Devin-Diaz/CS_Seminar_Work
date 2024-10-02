import requests

response = requests.get('https://api.thedogapi.com/v1/breeds/1')
print(response.json())
