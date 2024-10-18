import requests

# Your API key (replace 'your_api_key' with your actual API key)
API_KEY = '4c6566dad7dd46aab1b1eff96c08c955'

# Set the API endpoint for Premier League standings
url = "https://api.football-data.org/v4/competitions/PL/standings"

# Define headers with your API key
headers = {
    "X-Auth-Token": API_KEY
}

# Make the GET request to the Football-Data.org API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Example: Print the current standings (team names and positions)
    standings = data['standings'][0]['table']
    for team in standings:
        print(f"Position: {team['position']}, Team: {team['team']['name']}, Points: {team['points']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
