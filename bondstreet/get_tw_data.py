# ken wang
# xiankaiwang.sj@gmail.com
# 7/11/2016

# this module take a SME name and returns information retrived from facebook in a csv format
# usage
# command line args: 
# 1: business name to search, e.g. Chipotle, "Panera Bread", "Capital Grill" 
# 2: output file name (in csv format), this will be further processed by make_credit.py file
# e.g. python get_tw_data.py "Capital Grill" output_tw.csv


import tweepy
import sys
import numpy as np
import pandas as pd

consumer_key = 'F2Tdl4B4lQxDwC8jBOO2qAHvh'
consumer_secret = '4Y76P0Zpz1KEjK8ACkPFRuogkC6hMmpLehrmb1OtSv4oW6alJF'
access_token='77685274-UbH5IQ39VF2CkZOkOXM9x7pKGi4F4T4CNOp8QzqDq'
access_token_secret='m2nXB0TUXWgiGVUoPTvOhL5kX9XHpGHsAzQUbBHrZXDkm'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# api.update_status(status='using OAuth authentication via Tweepy')

# for tweet in tweepy.Cursor(api.search, q="indikitch", rpp=100, include_entities=True, lang="en").items(): 
#      ....
businessname = sys.argv[1]
l = [(str(x.created_at), x.text.encode('ascii','ignore').replace('\r',' ').replace('\n',' ')) for x in tweepy.Cursor(api.search, q=businessname, lang='en').items(100)]
df = pd.DataFrame(l, columns=['time','text'])


df.to_csv(sys.argv[2], index=False)


