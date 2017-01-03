


sort_dates = open("sort_date.txt","r").read().split("\n")

tweet_vols = open("tweet_vol.csv","r").read().split("\n")
tweet_cnt = {}

# print sort_dates

for item in tweet_vols:
    a = item.split(",")
    date = a[0]
    cnt = int(a[1])
    if(date not in tweet_cnt):
        tweet_cnt[date] = cnt
    else:
            tweet_cnt[date] = tweet_cnt[date] + cnt

# print tweet_cnt


for dates in sort_dates:
    if(dates in tweet_cnt):
        print dates+","+ str(tweet_cnt[dates])
    else:
        d2 = dates.replace("/2014","/14")
        d2 = dates.replace("/2015","/15")
        # print "~~~" + dates
        if(d2 in tweet_cnt):
            print d2+"," + str(tweet_cnt[d2])
            continue

    d3 = dates.replace("/1/","/01/")
    d3 = d3.replace("/2/","/02/")
    d3 = d3.replace("/3/","/03/")
    d3 = d3.replace("/4/","/04/")
    d3 = d3.replace("/5/","/05/")
    d3 = d3.replace("/6/","/06/")
    d3 = d3.replace('/7/','/07/')
    d3 = d3.replace("/8/","/08/")
    d3 = d3.replace("/9/","/09/")
    # print "~~~" + dates
    # print "~~~" + d3 + "~~" + dates
    if(d3 in tweet_cnt):
       print d3+"," + str(tweet_cnt[d3])

