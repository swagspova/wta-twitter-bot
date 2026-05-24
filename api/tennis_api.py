import requests

from config import TENNIS_API_KEY

BASE_URL = "https://api.api-tennis.com/tennis/"


def get_live_matches():

    params = {
        "method": "get_livescore",
        "APIkey": TENNIS_API_KEY,
        "event_type_key": "266",
        "timezone": "Asia/Kolkata"
    }

    response = requests.get(BASE_URL, params=params)

    print("Request URL:", response.url)

    if response.status_code != 200:
        print("API ERROR:", response.status_code)
        return None

    data = response.json()

    return data