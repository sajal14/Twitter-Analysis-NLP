
import xlrd
import pickle
from nltk import word_tokenize, pos_tag, ne_chunk
import re

users = {}

db = xlrd.open_workbook('../tweet_dataset.xlsx')
# f = open('simileys.txt',"r").readlines();



worksheet = db.sheet_by_index(0)

print(worksheet.cell(0, 0).value)

user_tweets = {}


for i in range(1,554356):
    name = str(worksheet.cell(i, 0).value)
    print name
    if name not in user_tweets:
        user_tweets[name.lower()] = [()]

    user_tweets[name.lower()].append((str(worksheet.cell(i,1)),str(worksheet.cell(i,2))))


# print user_tweets

pickle.dump(user_tweets, open("user_tweets_dates.p", 'wb'),-1)