#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wolf import Wolf
import json
import requests
import sys
import time
import tweepy
import wolframalpha
from keys import *

# authenticate with twitter & wolfram alpha
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# grab all tweets with "#tweetthewolf"
cursor = tweepy.Cursor(api.search, q="tweetthewolf")
for status in cursor.items():

    #if bot has not replied:
    #print("\n\n\nTWEEPY STATUS:\n" + json.dumps(status._json, indent=4, sort_keys=True))
    #try:
    print("status.text: " + str(status.text))

    wolf = Wolf(WOLFRAM_KEY, status.text)
    print(wolf.result())
    #print(json.dumps(wolf.request()["queryresult"]["pods"][1]["subpods"][0]["plaintext"], indent=2, separators=(',',':'), sort_keys=True))
    answer = str(wolf.request()["queryresult"]["pods"][1]["subpods"][0]["plaintext"])

    api.update_status(status=answer, in_reply_to_status_id = status.id)
    #except TweepError:
     #   print("\n\nlel.\n\n")

    '''
    res = client.query("12*12")#str(status.text))
    res = list(res)
    for n in res:
        print("\nbruh: " + str(n.text))
        #print("\n\n\nWOLFRAM|ALPHA RESULT:\n" + str(res.results[0].text))
    '''

    '''
    outfile = open('request.txt','w')
    outfile.write(str(status.id))
    outfile.close()

    infile = open('response.txt','r')
    f = infile.readlines()
    infile.close()

    #print("file:\n" + str(f[0]))
    '''
