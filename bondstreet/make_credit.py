# a toy credit score model based on public / social network information.
# ken wang
# xiankaiwang.sj@gmail.com
# 7/10/2016

# this file do process the data retrieved from various sources and make a simple toy credit score, without worrying about how these data are obtained. 
# usage: 

# python make_credit.py output_fb.csv


import numpy as np
import pandas as pd
import sys

# FB score
data_fb = pd.read_csv('output_fb.csv')

stores = len(data_fb)
median_likes = data_fb.likes.median()
median_checkins = data_fb.checkins.median() 

score_fb = 1.0 - 1.0 / np.sqrt( stores * median_checkins) - 1.0 / np.sqrt( stores * median_likes)
print score _fb







