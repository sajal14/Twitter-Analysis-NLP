
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import os
import pickle
import re


# users = open("temp_input_user4tweets.txt","r").read().split("\n")
# # print users
# c = Counter(users)
#
# out_file = open("user_tweet_count.csv","w")
#
# for key in c:
#     out_file.write(key + "," + str(c[key]) + "\n")


retweets = open("temp_retweet_cnt.txt","r").read().split("\n")
# print users
c = Counter(retweets)

out_file = open("retweet_count.csv","w")

for key in c:
    out_file.write(key + "," + str(c[key]) + "\n")
