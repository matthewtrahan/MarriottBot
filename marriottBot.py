import tweepy, time
from credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

marriottTweet = "I love being a Marriott member! Marriott for life! #MembersGetIt #RewardsPoints #FindYourRoute #MRpoints"

api.update_status(marriottTweet)
print(marriottTweet)
print('Tweet sent.')
