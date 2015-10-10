#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import keys

#enter the corresponding information from your Twitter application:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('response.txt','r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
