'''
Created on May 20, 2020

@author: noemi
'''

from datetime import datetime
import tweepy, credentials


if __name__ == '__main__':
    
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    api = tweepy.API(auth)
    
    api.update_status("test tweet")