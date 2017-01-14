from __future__ import unicode_literals
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
PUB_ID=os.environ.get('PUB_ID')

from jobs.job_ad import JobAd

from django.conf import settings


import sys  
import re

import urllib2
from textblob import TextBlob as tb
from BeautifulSoup import BeautifulSoup
import re
import requests
import unidecode
reload(sys)  
sys.setdefaultencoding('utf8')

class QuallyApiWrapper(object):
	
	
	
	@classmethod
	def get_job_ads(cls, user_query, start):
		base_url = "http://api.indeed.com/ads/apisearch?"
		publisher = "publisher="+ PUB_ID 
		# print publisher
		rq_options = "sort=&radius=&st=&jt=&start={}&limit=1000&fromage=&filter=&latlong=1&co=us&chnl=".format(start)
	
		#need to ask someone to help me/figure out get real user ip address and agent
		user_info="userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29"
		format_v= "v=2&format=json"

		#search_term and city, state need to be dynamically inserted

		"""user_query consists of
			yrs_exp			int
			search_term		string
			city			string
			state 			string"""
		search_term=user_query['search_term']
		city=user_query['city']
		state=user_query['state']

		# indeed_request_url= base_url+publisher+"&"+"q="+search_term+"&"+"l="+city+"%2C"+state+"&"+rq_options+"&"+user_info+"&"+format_v
		indeed_request_url= "{base}{pub}&q={search_term}&l={city}%2C{state}&{request_ops}&{user_info}&{version}".format(
			base=base_url,pub=publisher,search_term=search_term,city=city,state=state, request_ops=rq_options, user_info=user_info, version=format_v)
		# print "indeed request url: {}".format(indeed_request_url) 
		APIresponse=requests.get(indeed_request_url).json()['results']

		# print "API response: {}".format(APIresponse)
		return JobAd.make_job_ads_from_api(APIresponse)

	# def get_job_urls_batch(request_url):
 #    response = requests.get(request_url)
 #    json_data=response.json()
 #    job_ad_urls=[]
   
 #    for i, result in enumerate(json_data["results"]):
 #        # print result
 #        this_url= result["url"]
 #        job_ad_urls.append(this_url)  
 #        # print this_url
 #    return job_ad_urls

	# # gets num_records of job urls 
	# def get_mult_batches(request_url,num_records):
	#     start = 0
	#     batches =[]
	#     for i in range(((num_records-1)//25)+1):
	#        request_url=request_url.format(start)
	#        this_batch=get_job_urls_batch(request_url)
	#        batches.extend(this_batch)
	#        start+=25
	#     return batches









# job_ads=QuallyApiWrapper.get_job_ads({'search_term': 'software engineer',
# 						  					'city': 'seattle',
# 						  					'state': 'WA'})
# print "job ads: {}".format(job_ads)


# indeed_request_url="http://api.indeed.com/ads/apisearch?publisher=9253729351823762&q=software engineer&l=seattle%2C+wa&sort=&radius=&st=&jt=&start={}&limit=1000&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json"
# APIresponse = requests.get(indeed_request_url).json()['results']
# test_job_ads=JobAd.make_job_ads_from_api(APIresponse)
# print test_job_ads
# print len(test_job_ads)
# print type(test_job_ads)
# print type(test_job_ads[0])

# print dir(test_job_ads[0])
# print test_job_ads[0].content
	# print "hello"


