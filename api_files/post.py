import requests

url = 'https://api.thedogapi.com/v1/breeds'
headers = {'Content-Type': 'application/json'}

data = {
    "name": "Golden Retriever",
    "life_span": "10 - 12 years",
    "temperament": "Friendly, Intelligent, Devoted",
    "origin": "United Kingdom",
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Breed created successfully!")
else:
    print(f"Failed to create breed: {response.status_code}")
    print(response.json())

