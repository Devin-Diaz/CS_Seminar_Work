import requests

url = 'https://api.thedogapi.com/v1/breeds/1'  # Assuming '1' is the breed ID
headers = {'Content-Type': 'application/json'}

data = {
    "name": "Golden Retriever",
    "life_span": "12 - 14 years",  # Updating life span
    "temperament": "Friendly, Intelligent, Loyal",
    "origin": "United Kingdom",
}

response = requests.put(url, json=data, headers=headers)

if response.status_code == 200:
    print("Breed updated successfully!")
else:
    print(f"Failed to update breed: {response.status_code}")
    print(response.json())
