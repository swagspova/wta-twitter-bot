import requests
from config import TENNIS_API_KEY

BASE_URL = "https://api.api-tennis.com/tennis/"


def get_live_matches():
    url = f"{BASE_URL}?method=get_livescore&APIkey={TENNIS_API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        return None

    return response.json()