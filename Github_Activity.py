import requests
from datetime import datetime

username = input("Enter a github username:- ")
base_url = f"https://api.github.com/users/{username}/events"
try:
    response = requests.get(base_url)
except requests.exceptions.ConnectionError:
    print("Please check your Internet Connection")
    exit()

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

try:
    information = response.json()
except ValueError:
    print("Invalid response from Github")
    exit()

for event in information[:3]:
    time = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    print(f"{event['type']} in {event['repo']['name']} at {time.strftime('%b %d, %Y %H:%M')}")

