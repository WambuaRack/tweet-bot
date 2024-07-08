import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
import random
import time

# Twitter API credentials
# Twitter API credentials (replace with your regenerated tokens)
API_KEY = 'your_new_api_key'
API_SECRET_KEY = 'your_new_api_secret_key'
ACCESS_TOKEN = 'your_new_access_token'
ACCESS_TOKEN_SECRET = 'your_new_access_token_secret'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# List of Martin Luther King Jr. quotes
quotes = [
    "The time is always right to do what is right.",
    "Injustice anywhere is a threat to justice everywhere.",
    "Life's most persistent and urgent question is, 'What are you doing for others?'",
    "The arc of the moral universe is long, but it bends towards justice.",
    "I have decided to stick with love. Hate is too great a burden to bear.",
    "Faith is taking the first step even when you don't see the whole staircase."
]

# Function to tweet
def tweet():
    try:
        # Select a random quote
        quote = random.choice(quotes)
        
        # Tweet the selected quote
        api.update_status(quote)
        print("Tweeted: " + quote)
    except tweepy.TweepError as e:
        print(f"Error occurred: {e}")

# Scheduler setup
scheduler = BlockingScheduler()

# Add a job to the scheduler that runs every 2 seconds
scheduler.add_job(tweet, 'interval', seconds=2)

# Start the scheduler
print("Starting the tweet scheduler...")
scheduler.start()

# Keep the script running
while True:
    time.sleep(1)
