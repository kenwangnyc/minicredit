# ken wang
# xiankaiwang.sj@gmail.com
# 7/10/2016

# this module take a SME name and returns information retrived from facebook in a csv format
# usage
# command line args: 
# 1: business name to search, e.g. Chipotle, "Panera Bread", "Capital Grill" 
# 2: output file name (in csv format), this will be further processed by make_credit.py file
# e.g. python get_fb_data.py "Capital Grill" output_fb.csv


# facebook graph API usage example : 

# short lived token can be obtained from graph api explorer, long-lived through developer registration. 
# IMPORTANT NOTE: short-lived token can get more detailed page information but long-lived can only get name and id... why ? ??? 
# graph= x = graph.request('search?q=indikitch&type=place')
# x is a dict w/ 2 keys, paging and data, 
# data is a list of nodes w/ each store's information, including address (st #, zip, latitude, longitude, id) 
# get single store w/ a id (returned from the search result data), graph.get_object(id='####') #### is the id number e.g. 669945423110940
# useful quantitative information: checkins / were_here_count, likes, price_range, 


import facebook as fb
import numpy as np
import pandas as pd
import sys
# mytoken = '1932258216801125|2DvQ5-S-U5RA_SHo-w9iMwI0P50'  # long-lived token, no page detail when graph.get_objects(id=...), switch to short-lived
mytoken ='EAACEdEose0cBAPKswAgkZCBHD5qudIGyN3kgZBUuB5b3KZCHbp1tbMo8jKVOGDKM8G4BBgxbMReaSpcKYbLximGxnhKTBytcBwZCw62M04tPRbPNphGsANzdX2WlqoxZAw2Cel3nvTpjJipxfP9k9ZAXBboL2PGy5H0Ti0QfJzAwZDZD' 
# can be re-generated through dveloper explorer, with a different user
# this expires within one day, how to generate long-lived token ?? 

graph=fb.GraphAPI(mytoken)
# print graph.get_object('me')
businessname = sys.argv[1]

req = graph.request('search?q=' + businessname + '&type=place')
ids = [x['id'] for x in req['data']]   #  if x['location']['country'].lower()==u'united states']
l = [[x['id'], x['checkins'], x['were_here_count'], x['likes']] for x in graph.get_objects(ids).values()]
df = pd.DataFrame(l, columns=['id','checkins','were_here_count','likes'])

df.to_csv(sys.argv[2], index=False)


