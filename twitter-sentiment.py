import tweepy #python library for accessing Twitter API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob

#import twitter_credentials
import pandas as pd
import numpy as np

def sentimentTwitter(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
    AUTH = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    API = tweepy.API(AUTH)
    public_tweets = API.search('Rihana')
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)

        if analysis.sentiment[0]>0:
            print('The sentiment of the tweet is positive')
        else:
            print('The sentiment of the tweet is negative')



def main():
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    sentimentTwitter(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


if __name__ == '__main__':
    main()
