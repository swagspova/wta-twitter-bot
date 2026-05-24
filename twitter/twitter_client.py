import tweepy
from config import (
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)


def send_tweet(message):

    try:
        response = client.create_tweet(text=message)
        return response

    except Exception as e:
        print("Tweet error:", e)
        return None