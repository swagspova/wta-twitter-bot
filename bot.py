from twitter.twitter_client import send_tweet

message = "🎾 WTA Twitter Bot is now live."

response = send_tweet(message)

print("Tweet sent successfully!")
print(response)