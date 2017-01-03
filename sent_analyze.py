
import xlrd
from vaderSentiment.vaderSentiment import sentiment as vs
import pickle
#

db = xlrd.open_workbook('../tweet_dataset.xlsx')
worksheet = db.sheet_by_index(0)

data = {}

sentiment_out = open("sentiment_tweets2.csv","w")
sentiment_out.write("User\ttweet\tdate\tnegative\tneutral\tpositive\tcompound\n")

for i in range(1,554356):
    user = worksheet.cell(i,0).value
    tweet = worksheet.cell(i,1).value
    date = worksheet.cell(i,2).value
    sent_anal = vs(tweet)
    sentiment_out.write("\t".join([user,tweet,date,str(sent_anal["neg"]),str(sent_anal["neu"]),str(sent_anal["pos"]),str(sent_anal["compound"])]))
    sentiment_out.write("\n")
