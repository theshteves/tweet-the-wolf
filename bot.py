#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys
import time
import tweepy
import wolframalpha
from keys import *
from tweepy.error import TweepError
from wolf import Wolf


# authenticate with twitter & wolfram alpha
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# grab all tweets with "#tweetthewolf"
cursor = tweepy.Cursor(api.search, q="tweetthewolf")
for status in cursor.items():

    #print(json.dumps(status._json, indent=2, separators=(',',':'), sort_keys=True))

    try:
        print("status.text: " + str(status.text))

        wolf = Wolf(WOLFRAM_KEY, status.text)
        print(wolf.result())
        # For debugging:
        # print(json.dumps(wolf.request()["queryresult"]["pods"][1]["subpods"][0]["plaintext"], indent=2, separators=(',',':'), sort_keys=True))
        answer = str(wolf.request()["queryresult"]["pods"][1]["subpods"][0]["plaintext"])
        answer = "@" + status._json[0]["screen_name"] + " " + answer

    except TweepError as err:
        print("TweepError: " + str(err))
        continue

    except KeyError as err:
        print("KeyError: " + str(err))
        continue

    else:
        api.update_status(status=answer, in_reply_to_status_id = status.id)

    finally:
        print("\n")
