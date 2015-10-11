#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys
import time
import tweepy
from keys import *
from tweepy.error import TweepError
from wolf import Wolf

# sys.setdefaultencoding("utf-8")

# authenticate with twitter & wolfram alpha
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# grab all tweets with "#tweetthewolf"
cursor = tweepy.Cursor(api.search, q="tweetthewolf")
for status in cursor.items():

    try:
        print("TWEET: " + str(status.text))
        print("FROM:  " + str(status._json["user"]["screen_name"]))

        wolf = Wolf(WOLFRAM_KEY, status.text)
        print("REQUEST URL: " + wolf.result())

        res = wolf.request()["queryresult"]
        if res["success"] and res.get("pods"):
            answer = ""

            for pod in res["pods"]:
                if pod["subpods"][0]["plaintext"] and len(pod["subpods"][0]["plaintext"] + answer) < 110:
                    answer += pod["subpods"][0]["plaintext"] + "\n"


            # tag questioner in response
            answer = "@" + status._json["user"]["screen_name"] + " " + answer
            print("ANSWER: " + answer)

        else:
            raise TweepError("RequestError: Wolfram|Alpha query was unsuccessful")


    except TweepError as err:
        print("TweepError: " + str(err))
        continue

    except KeyError as err:
        print("KeyError: " + str(err))
        continue

    else:
        api.update_status(status=answer, in_reply_to_status_id = status.id)

    finally:
        #print()
        pass
