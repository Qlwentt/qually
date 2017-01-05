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


# #0 for bumpy, 1 for smooth
# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# #0 for apple, 1 for orange
# labels = [0, 0, 1, 1]

# classifier= tree.DecisionTreeClassifier()

# classifier= classifier.fit(features,labels)

# print classifier.predict([[160,0]])


#term frequency is the number of times a word appears in a text file (textfile), 
#normalized (averaged) by dividing by the total number of words in that file. 

#TextBlob will break the textfile into words and get the word counts
def tf(word, textfile):
    return textfile.words.count(word) / len(textfile.words)

#returns the number of documents containing word. 
#A generator expression is passed to the sum() function.

#text files is a list of text files
def n_containing(word, textfiles):
    return sum(1 for textfile in textfiles if word in textfile.words)

#computes "inverse document frequency" which measures 
#how common a word is among all documents in textfile_list. 
#The more common a word is, the lower its idf. 

#We take the ratio of the total number of documents 
#to the number of documents containing word, then take the log of that. 

#Add 1 to the divisor to prevent division by zero.

def idf(word, textfiles ):
	#bottom = (1 + n_containing(word, textfiles))
	# print "bottom: {}".format(bottom)

	#top = len(textfiles)
	# print "top: {}".format(top)

	#num = math.log((3)/4)
	# print "log: {}".format(num)

	result = math.log((len(textfiles)) / (1 + n_containing(word, textfiles)))
	# print "result: {}".format(result)
	return result

#computes the TF-IDF score. It is simply the product of  tf and idf.
def tfidf(word, texfile, textfiles):
    return tf(word, texfile) * idf(word, textfiles)

########
# Request to Indeed API for job ad list should go here
def get_job_ad_urls(num_records):
    start = 0
    for i in range((num_records-1)//25):
        print "start: {}".format(start)
        start+=25


get_job_ad_urls(100)
(num_records-1)/25
indeed_request_url="http://api.indeed.com/ads/apisearch?publisher=9253729351823762&q=software engineer&l=seattle%2C+wa&sort=&radius=&st=&jt=&start=0&limit=1000&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json"
# indeed_request_url+=.format(num_times)
response = requests.get(indeed_request_url)
print response.status_code
print response.headers['content-type']
# print "Number of results: {}".format(len(response.json()["results"]))
json_data=response.json()
# Get url of a job ad from Indeed API response
job_ad_url= json_data["results"][0]["url"]
print job_ad_url
#########

# get get text from job ad url

#test_url = "https://jobs.lever.co/palantir/7a2cf40e-ab26-4b14-ae1d-0919625816ce"
html = urllib2.urlopen(job_ad_url).read()



# tidy, errors = tidy_document(html)
# # soup = BeautifulSoup(tidy)
soup = BeautifulSoup(html)


texts = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

visible_texts = filter(visible, texts)
job_ad = ' '.join(visible_texts)

print job_ad

job_ad_nouns = tb(job_ad).noun_phrases
# print "Nouns:{}".format(job_ad_nouns) 




# job_ad_nouns=' '.join(job_ad_nouns)
# print job_ad_nouns
# document1 = tb(job_ad_nouns)

# document2 = tb("""Python, from the Greek word blahblah, is a genus of
# nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
# recognised.[2] A member of this genus, P. reticulatus, is among the longest
# snakes known.""")

# document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
# manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
# It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
# in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued
# Colt Python targeted the premium revolver market segment. Some firearm
# collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
# Thompson, Renee Smeets and Martin Dougherty have described the Python as the
# finest production revolver ever made.""")

# textfiles = [document1, document2, document3]
# for i, textfile in enumerate(textfiles):
#     print("Top words in document {}".format(i + 1))
#     scores = {word: tfidf(word, textfile, textfiles) for word in textfile.words}
#     sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#     for word, score in sorted_words[:100]:
#         print("\tWord: {}, TF-IDF: {}".format(tb(word), round(score, 5)))






