import requests

API_KEY = 'API_KEY_HERE'

url = f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=1"

response = requests.get(url)

data = response.json()

# Extract the first trending gif
if 'data' in data and len(data['data']) > 0:
    gif_url = data['data'][0]['url']
    print(f"Trending GIF: {gif_url}")
else:
    print("No GIFs found")
