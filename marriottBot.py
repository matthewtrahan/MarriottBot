import tweepy, time, random
from credentials import *
from random import choice

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

phrases = ["Allegedly", "Wubbalubbadubdub", "Schlim Schlam Schlippidy Doo", "I love Marriott", "Hook 'Em", "H-Town"]

marriottTweet = random.choice(phrases) + " #MembersGetIt #RewardsPoints #FindYourRoute #MRpoints"

api.update_status(marriottTweet)
print(marriottTweet)
print('Tweet sent.')
