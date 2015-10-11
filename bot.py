#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

infile = open('response.txt','r')
f = infile.readlines()
infile.close()

cursor = tweepy.Cursor(api.search, q="tweetthewolf")
#print("cursor:\n" + str(cursor.items()))

for status in cursor.items():

    #if bot has not replied:
    print("status:\n" + str(status.id))
    print("file:\n" + str(f[0]))
    outfile = open('request.txt','w')
    outfile.write(str(status.id))
    outfile.close()

    #api.update_status(status=str(f[0]), in_reply_to_status_id = status.id)
