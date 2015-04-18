#! /usr/bin/env python

import sys
import tweepy
import random

# OAuth stuff

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Open file and select tweet
LIST_PATH = ''

master = open(LIST_PATH)
tweet_list = master.readlines()
random_tweet = tweet_list[random.randint(0, len(tweet_list)-1)]

# Break up tweet into <140 character chunks (no more than 2)

tweet_chunks = []

if len(random_tweet) <= 140:
	tweet_chunks.append(random_tweet)
else:
	breakpoint = random_tweet.rfind(' ', 0, 140)
	tweet_chunks.append(random_tweet[:breakpoint + 1])
	tweet_chunks.append(random_tweet[breakpoint + 1:])

# Tweet it!

for chunk in tweet_chunks:
	api.update_status(chunk)

