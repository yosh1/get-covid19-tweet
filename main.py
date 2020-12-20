# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
import tweepy

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_key = os.environ.get("ACCESS_KEY")
access_secret = os.environ.get("ACCESS_SECRET")
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
 
q = "コロナ 元気"
count = 1000000000
files = "./train.txt"
tweet_list= ''
 
tweets = api.search(q=q, locale="ja", count=count,tweet_mode='extended')
for tweet in tweets:
    if 'RT' not in tweet.full_text:
      if '@' not in tweet.full_text:
        if 'http' not in tweet.full_text:
            print(tweet.full_text.replace('\n', ''))
            tweet_list = tweet_list + tweet.full_text.replace('\n', '') + '\n'
file = open(files, 'a')
file.write(tweet_list)
