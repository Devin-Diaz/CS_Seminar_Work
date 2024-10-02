import requests

url = 'https://api.thedogapi.com/v1/breeds/1'  # Assuming '1' is the breed ID to delete
headers = {'Content-Type': 'application/json'}

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print("Breed deleted successfully!")
else:
    print(f"Failed to delete breed: {response.status_code}")
    print(response.json())
