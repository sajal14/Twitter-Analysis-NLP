
import xlrd
import pickle
from nltk import word_tokenize, pos_tag, ne_chunk
import re

def write_smiley_count(user_tweets):

    smiley = open("simileys.txt","r").read().split("\n")

    user_smiley = {}

    for key in user_tweets:
        user_smiley[key] = 0


    smiley_out = open("user_smiley.csv","w")
    smiley_out.write("users,")
    smiley_out.write(",".join(smiley))
    smiley_out.write("\n")

    for user in user_tweets:
        tweets = user_tweets[user];
        # print len(tweets)
        alltweets = ""
        alltweets = " #### ".join(tweets)
        allwords = alltweets.split()
        row = user

        for s in smiley:
            print s.strip()
            c = allwords.count(s.strip())
            row = row + "," + str(c)

        row += "\n"
        smiley_out.write(row)



def write_education_words(user_tweets):
    education = open("education_words.txt","r").read().split("\n")

    user_education = {}

    for key in user_tweets:
        user_education[key] = 0


    smiley_out = open("user_education.csv","w")
    smiley_out.write("users,")
    smiley_out.write(",".join(education))
    smiley_out.write("\n")

    for user in user_tweets:
        tweets = user_tweets[user];
        # print len(tweets)
        tweets = [x.lower() for x in tweets]
        alltweets = " #### ".join(tweets)
        # allwords = alltweets.split()
        row = user

        for s in education:
            print s.strip()
            c = alltweets.count(s.strip())
            row = row + "," + str(c)

        row += "\n"
        smiley_out.write(row)



def write_politic_words(user_tweets):
    politic = open("political_words.txt","r").read().split("\n")

    user_education = {}

    for key in user_tweets:
        user_education[key] = 0


    smiley_out = open("user_politics.csv","w")
    smiley_out.write("users,")
    smiley_out.write(",".join(politic))
    smiley_out.write("\n")

    for user in user_tweets:
        tweets = user_tweets[user];
        # print len(tweets)
        tweets = [x.lower() for x in tweets]
        alltweets = " #### ".join(tweets)
        # allwords = alltweets.split()
        row = user

        for s in politic:
            print s.strip()
            c = alltweets.count(s.strip())
            row = row + "," + str(c)

        row += "\n"
        smiley_out.write(row)



def write_1st_3rd_persons(user_tweets): #NO STRIP FOR INPUT WORDS
    politic = open("affiliation.txt","r").read().split("\n")

    user_education = {}

    for key in user_tweets:
        user_education[key] = 0


    smiley_out = open("affiliation.csv","w")
    smiley_out.write("users,sum,total_tweets,proportion,")
    smiley_out.write(",".join(politic))
    smiley_out.write("\n")

    for user in user_tweets:
        tweets = user_tweets[user];
        # print len(tweets)
        tweets = [x.lower() for x in tweets]
        alltweets = " #### ".join(tweets)
        # allwords = alltweets.split()
        row = user

        su = 0;
        # prop = 0.0;
        words = ""
        for s in politic:
            # print s.strip()
            c = alltweets.count(s)
            su = su+c;
            if (words == ""):
                words = str(c)
            else:
                words = words + "," + str(c);

            # row = row + "," + str(c)

        row = row + "," + str(su);
        row = row +"," + str(len(tweets))
        row = row +"," + str((su+0.0)/len(tweets));
        row = row + "," + words;

        row += "\n"
        smiley_out.write(row)

def prop_greater_n(user_tweets,n):

    out = open("word_len_gr6.csv","w")
    out.write("users,total_words,word_length_gr6,proportion")

    for user in user_tweets:
        tweets = user_tweets[user];
        tweets = [x.lower() for x in tweets]
        # tweets = tweets.encode('utf-8')
        tweet_cnt = len(tweets)
        alltweets = " #### ".join(tweets)
        alltweets = re.sub(r'(\\x[a-z]\d)'," ", alltweets)
        # alltweets = alltweets.encode('utf-8')
        # alltweets = alltweets.replace("text:u","")
        allwords = alltweets.split()
        word_cnt = len(allwords) - (tweet_cnt - 1)
        # print len(allwords)
        # tot = len(allwords)
        cnt = 0.0

        out.write("\n")
        for word in allwords:
            if len(word) > n:
                cnt = cnt+1
        out.write(str(user) + "," + str(word_cnt) + "," + str(cnt) + "," + str(cnt/word_cnt))
        out.write('\n')
        print user

    out.close()

def verbTenseTag(user_tweets):

    out = open("verb_tense.csv","w")
    out.write("user,sum,total_tweets,proportion,VB,VBD,VBG,VBN,VBP,VBZ\n")
    i = 1
    for user in user_tweets:
        tweets = user_tweets[user];
        alltweets = " ".join(tweets)
        alltweets = alltweets.replace("text:u","")
        # print pos_tag(word_tokenize(alltweets))
        # print pos_tag(alltweets.split())
        # print tweets
        pos_tags = pos_tag(word_tokenize(alltweets))
        vb = 0
        vbd = 0
        vbg = 0
        vbn = 0
        vbp = 0
        vbz = 0
        out.write(user + ",")
        for tag_tups in pos_tags:
            if(tag_tups[1] == 'VB'):
                vb +=1
            if(tag_tups[1] == 'VBD'):
                vbd +=1
            if(tag_tups[1] == 'VBG'):
                vbg +=1
            if(tag_tups[1] == 'VBP'):
                vbp +=1
            if(tag_tups[1] == 'VBN'):
                vbn +=1
            if(tag_tups[1] == 'VBZ'):
                vbz +=1
        print i
        i +=1
        su = 0.0
        su = su +vb+vbd+vbg+vbn+vbp+vbz;
        out.write(str(su) + "," + str(len(tweets)) + "," + str(su/len(tweets)) + "," + str(vb) + "," + str(vbd) + "," + str(vbg) + "," + str(vbn) + "," + str(vbp) + "," + str(vbz) +"\n")

    out.close()

def nouns_proportion(user_tweets):
    out = open("nouns_proportion.csv","w")
    out.write("users,total_words,total_nouns,proportion")

    for user in user_tweets:
        tweets = user_tweets[user];
        tweets = [x.lower() for x in tweets]
        # tweets = tweets.encode('utf-8')
        tweet_cnt = len(tweets)
        alltweets = " #### ".join(tweets)
        alltweets = re.sub(r'(\\x[a-z]\d)'," ", alltweets)
        # alltweets = alltweets.encode('utf-8')
        # alltweets = alltweets.replace("text:u","")
        allwords = alltweets.split()
        word_cnt = len(allwords) - (tweet_cnt - 1)

        tagged = pos_tag(allwords)

        # print len(allwords)
        # tot = len(allwords)
        cnt = 0.0

        out.write("\n")
        for word in allwords:
            if len(word) > n:
                cnt = cnt+1
        out.write(str(user) + "," + str(word_cnt) + "," + str(cnt) + "," + str(cnt/word_cnt))
        out.write('\n')
        print user

    out.close()



def proportion_using_total_words(user_tweets): #NO STRIP FOR INPUT WORDS
    politic = open("Set_4/Noun words.txt","r").read().split("\r")
    print politic
    user_education = {}

    for key in user_tweets:
        user_education[key] = 0


    smiley_out = open("Set_4/Noun words Analysis.csv","w")
    smiley_out.write("users,sum,total words,proportion,")
    smiley_out.write(",".join(politic))
    smiley_out.write("\n")

    for user in user_tweets:
        tweets = user_tweets[user];
        # print len(tweets)
        tweets = [x.lower() for x in tweets]
        # for tweet in tweets:
        #     tweet = re.sub(r'(\\x[a-z]\d)'," ", tweet)

        tweet_cnt = len(tweets)

        alltweets = " #### ".join(tweets)
        # alltweets = alltweets.decode("utf-8")
        alltweets = re.sub(r'(\\x[a-z]\d)'," ", alltweets)
        # alltweets = re.sub(r'.'," ", alltweets)
        all_words_in_tweet = alltweets.split();
        word_cnt = len(all_words_in_tweet) - (tweet_cnt - 1)
        # allwords = alltweets.split()
        row = user

        su = 0;
        # prop = 0.0;
        words = ""
        for s in politic:
            # print 1
            # print s.strip()
            # c = alltweets.count(s)
            c = all_words_in_tweet.count(s)
            su = su+c;
            if (words == ""):
                words = str(c)
            else:
                words = words + "," + str(c);

            # row = row + "," + str(c)

        row = row + "," + str(su);
        row = row +"," + str(word_cnt)
        row = row +"," + str((su+0.0)/word_cnt);
        row = row + "," + words;

        row += "\n"
        smiley_out.write(row)



def get_proportion_by_date(user_tweets_dates,for_date): #NO STRIP FOR INPUT WORDS
    politic = open("Set_1/We Words Library.txt","r").read().split("\r")
    # print politic
    # user_education = {}
    #
    # for key in user_tweets_dates:
    #     user_education[key] = 0

    # book = xlrd.open_workbook("/Users/sajal/RA/tweet_dataset.csv")

    smiley_out = open("UserDatesEvent/We/30-04.csv","w+")
    smiley_out.write("users,total_words, word_list_word,proportion")
    # smiley_out.write(",".join(politic))
    smiley_out.write("\n")

    for user in user_tweets_dates:
        tweets_dates = user_tweets_dates[user]; #0th element is list of tweets

        all_tweets_for_date = ""
        tweet_cnt = 0
        for pairs in tweets_dates:
            if(len(pairs) != 2):
                continue

            tweet = pairs[0].decode("utf-8")
            date = pairs[1].decode("utf-8")
            # print(date)

            # date,month,year = xlrd.xldate_as_tuple(date, book.datemode);
            # print(date,month,year)
            if (for_date in date):
                # print "11" + tweet
                all_tweets_for_date += " #### " + tweet
                tweet_cnt += 1
                # print date

        # print all_tweets_for_date
        all_tweets_for_date = all_tweets_for_date.decode("utf-8")

        all_tweets_for_date = re.sub(r'(\\x[a-z]\d)'," ", all_tweets_for_date)
        # alltweets = re.sub(r'.'," ", alltweets)
        all_words_in_tweet = all_tweets_for_date.split();
        print all_words_in_tweet
        word_cnt = len(all_words_in_tweet)
        # # allwords = alltweets.split()

        print word_cnt
        row = user
        #
        su = 0;
        # prop = 0.0;
        words = ""
        for s in politic:
            # print 1
            # print s.strip()
            # c = alltweets.count(s)
            c = all_words_in_tweet.count(s)
            su = su+c;
            # if (words == ""):
            #     words = str(c)
            # else:
            #     words = words + "," + str(c);

            # row = row + "," + str(c)

        # row = row + "," + str(su);
        # row = row +"," + str(word_cnt)
        if(word_cnt != 0):
            row = row +"," + str(word_cnt) + "," + str(su) + "," + str((su+0.0)/word_cnt);
        else:
            row = row +"," + str(word_cnt) + "," + str(su) + "," + "NA";
        # row = row + "," + words;

        row += "\n"
        smiley_out.write(row)






if __name__ == "__main__":

    # user_tweets = pickle.load(open("user_tweets.p", 'rb'))

    # print user_tweets["AdvocateforEd"]

    user_merged_dates_tweets = {}

    # for key in user_tweets:
    #     lowKey = key.lower()
    #     if lowKey in user_merged_tweets:
    #         user_merged_tweets[lowKey].extend(user_tweets[key])
    #     else:
    #         user_merged_tweets[lowKey] = user_tweets[key]
    #
    # pickle.dump(user_merged_tweets, open("user_merged_tweets.p", 'wb'),-1)

    user_merged_dates_tweets = pickle.load(open("user_tweets_dates.p", 'rb'))
    # print user_merged_dates_tweets

    get_proportion_by_date(user_merged_dates_tweets, "30/04/2015")
    # print user_merged_tweets["advocatefored"]


    # write_1st_3rd_persons(user_merged_tweets)
    # proportion_using_total_words(user_merged_tweets)
    # prop_greater_n(user_merged_tweets,6)

    # verbTenseTag(user_merged_tweets)




    # write_smiley_count(user_tweets)

    # write_education_words(user_tweets)

    # write_politic_words(user_tweets)
    # write_1st_3rd_persons(user_tweets)

        #
        # if(s in alltweets):
        #     print s
        #     alltweets.count(s)
        #     # user_smiley[user] = user_smiley[user]+ alltweets.count(s)
        # else:


# print user_smiley





#Similar for list of positive words


#Similar for list of negative words


