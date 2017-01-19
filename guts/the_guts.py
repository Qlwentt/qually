# _*_ coding:utf-8 _*_
from __future__ import division
from sklearn import tree
import math
from textblob import TextBlob as tb

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import scrapy 
import urllib2
from tidylib import tidy_document
import re

import blockspring
import json
import unidecode
import requests


#term frequency is the number of times a word appears in a text file (textfile), 
#normalized (averaged) by dividing by the total number of words in that file. 

#TextBlob will break the textfile into words and get the word counts
def tf(word, textfile):
    return textfile.words.count(word) / len(textfile.words)


#returns the number of documents containing word. 
#A generator expression is passed to the sum() function.

#text files is a list of text files
# number of text files that have these words
def n_containing(word, textfiles):
    return sum(1 for textfile in textfiles if word in textfile.words)

# take most common queries (software engineer, data scientist,etc. ) and pre compute keyword frequency to reduce runtime
# replace above with..



#computes "inverse document frequency" which measures 
#how common a word is among all documents in textfile_list. 
#The more common a word is, the lower its idf. 

#We take the ratio of the total number of documents 
#to the number of documents containing word, then take the log of that. 

#Add 1 to the divisor to prevent division by zero.

def idf(word, textfiles ):

    result = math.log((len(textfiles)) / (1 + n_containing(word, textfiles)))
    # print "result: {}".format(result)
    return result




#computes the TF-IDF score. It is simply the product of  tf and idf.
def tfidf(word, texfile, textfiles):
    return tf(word, texfile) * idf(word, textfiles)





########
# Request to Indeed API given a request url
# parameters will be changed according to user input
# right now it is hard coded

indeed_request_url="http://api.indeed.com/ads/apisearch?publisher=9253729351823762&q=software engineer&l=seattle%2C+wa&sort=&radius=&st=&jt=&start={}&limit=1000&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json"

# gets one batch (25) job ad urls
def get_job_urls_batch(request_url):
    response = requests.get(request_url)
    json_data=response.json()
    job_ad_urls=[]
   
    for i, result in enumerate(json_data["results"]):
        # print result
        this_url= result["url"]
        job_ad_urls.append(this_url)  
        # print this_url
    return job_ad_urls

# gets num_records of job urls 
def get_mult_batches(request_url,num_records):
    start = 0
    batches =[]
    for i in range(((num_records-1)//25)+1):
       request_url=request_url.format(start)
       this_batch=get_job_urls_batch(request_url)
       batches.extend(this_batch)
       start+=25
    return batches

# call get_mult_batches to get 100 job urls 
these_batches = get_mult_batches(indeed_request_url,10)


print "10 job urls: {}".format(these_batches[:1])


def fix_spacing(text):
    return re.sub(r'([a-z:.)])([A-Z])', r'\1 \2', text)
    
# Get url of a job ad from Indeed API response


#########
def get_job_text_list(job_ad_url_list):
    # get get text from  job ad urls
    job_text_list=[]
    for i, job_ad_url in enumerate(job_ad_url_list):
        html = urllib2.urlopen(job_ad_url).read()
        soup = BeautifulSoup(html)
        job_ad_text = soup.find('span', attrs={'id': 'job_summary'}).text
        job_ad_text=fix_spacing(job_ad_text)
        # print "\n"
        # print job_ad_text
        # print "\n" 
        job_text_list.append(job_ad_text)
    return job_text_list

def get_noun_list(text_list):
    noun_list=[]
    for i, text in enumerate(text_list):

        # get all the nouns out of job_ad_text
        job_ad_nouns = tb(text).noun_phrases
        # print "Unicode list of job ad noun phrases:{}".format(job_ad_nouns) 

        #change list to string
        job_ad_nouns=' '.join(job_ad_nouns)
        # print job_ad_nouns
        noun_list.append(tb(job_ad_nouns))

    return noun_list

job_text_list1=get_job_text_list(these_batches[:2])

print job_text_list1[0]
print tb(job_text_list1[0]).sentences

noun_list=get_noun_list(job_text_list1)

# document1 = tb(noun_list[0])

# document2 = tb(noun_list[1])

# document3 = tb(noun_list[2])



textfiles = noun_list
for i, textfile in enumerate(textfiles):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, textfile, textfiles) for word in textfile.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("\tWord: {}, TF-IDF: {}".format(tb(word), round(score, 5)))









