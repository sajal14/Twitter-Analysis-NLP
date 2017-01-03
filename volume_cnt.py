import xlrd
from vaderSentiment.vaderSentiment import sentiment as vs
import pickle
import re
#
#
# db = xlrd.open_workbook('../tweet_dataset.xlsx')
# worksheet = db.sheet_by_index(0)

# db = open("../tweet_dataset.csv").read()
# lines = db.split("\n")
# print len(lines)

f_dates = open("tweet_dates.txt","r").read()

dates = f_dates.split("\n")
date_cnt = {}

tweet_vol = open("tweet_vol.csv","w")

for date in dates:

    if "/14" in date :
        date = date[0:len(date)-2]
        date = date + "2014"
    if "/15" in date :
        date = date[0:len(date)-2]
        date = date + "2015"
    if date in date_cnt:
        date_cnt[date] = date_cnt[date]+1
    else:
        date_cnt[date] = 1


print len(date_cnt)

for d in date_cnt:
    a = d.split("/")
    if(len(a) >1):
        print a
        m = int(a[1])
        print m
        if(m >=1 and m<=12):
            tweet_vol.write(str(d) + "," + str(date_cnt[d])+"\n")



#
# for line in lines:
#     a = re.findall("(\d{1,2}[/]\d{1,2}[/]\d{0,2}(14|15))",line)
#     # print len(a)
#     if(a):
#         # print line
#
#         leng = len(a)
#         print a[0][0]
#         f_dates.write(a[0][0]+"\n")
#     else:
#         f_dates.write(str(None)+"\n")

#
# volume_out = open("volume_cnt.csv","w")
# volume_out.write("date\n")
#
#
# for i in range(1,554356):
#     tweet = str(worksheet.cell(i,1))
#     # print worksheet.cell(i,2).value
#     date = str(worksheet.cell(i,2))
#     tweetdate = ""
#     # if(isinstance(date,basestring) == False):
#     #     tweetdate = tweet
#     # else:
#     tweetdate = tweet + " #### " + date
#     a = re.findall("(\d{1,2}[/]\d{1,2}[/]\d{2,4})",tweetdate)
#     if a:
#         volume_out.write(a[0]+"\n")
#     else:
#         print tweetdate
#         volume_out.write("None\n")
