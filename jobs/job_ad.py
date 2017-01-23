# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from collections import defaultdict

import sys  
import unidecode
import re

import urllib2
from textblob import TextBlob as tb
from BeautifulSoup import BeautifulSoup
import re
import requests
import unidecode

from jobs.models import Keyword, CachedJob


reload(sys)  
sys.setdefaultencoding('utf8')



class JobAd(object):
	"""" A job ad from the Indeed API. It has the following properties:
	Attributes:
		# id: unique identitfier 		integer
		key: unique id for API 		string
		title: title of job ad; 	string
		snippet: short description; string
		url: url of full ad; 		string
		company: company name;		string
		content: full content of ad string 
		location: City, State;		string
		date: date posted;			datetime
	"""


	def __init__(self, properties):
		#Returns job ad object with properties
		self.key=properties['key']
		self.title=properties['title']
		self.snippet=properties['snippet']
		self.content=''
		self.url=properties['url']
		self.company=properties['company']
		self.location=properties['location']
		self.date=properties['date']
		self.score=0
		self.matching_words=[]
		self.exp_req=0
		self.qually_rec = False

	@staticmethod
	def fix_spacing(text):
		  text=re.sub(r'([a-z:.)])([A-Z]|\d\W)', r'\1 \2', text)
		  text=text.decode("utf-8").replace(u"\u2022", " ").encode("utf-8")
		  return text

	@classmethod
	def make_job_ads_from_api(cls,api_json_resp):
		job_ads=[]
			
		for result in api_json_resp:
			# print "result: {}".format(result)
			# print "result type: {}".format(type(result[0]))
			job_ads.append(JobAd({
				'key': result['jobkey'],
				'title': result['jobtitle'],
				'snippet': result['snippet'],
				'url': result['url'],
				'company': result['company'],
				'location': result['formattedLocation'],
				'date': result['date']
				})) 
		for job_ad in job_ads:
			try:
				cj=CachedJob.objects.get(key=job_ad.key)
				job_ad.content = cj.content
			except CachedJob.DoesNotExist:  
				job_ad.content=job_ad.set_content()

		return job_ads
	
	def set_content(self):	
	    # self.content=job_ad_text
	    html = urllib2.urlopen(self.url).read()
	    soup = BeautifulSoup(html)
	    job_ad_text = soup.find('span', attrs={'id': 'job_summary'}).text
	    job_ad_text= JobAd.fix_spacing(job_ad_text)
	    return job_ad_text

	@staticmethod
	def to_s(tb):
		return ('\t' + str(tb))

	@staticmethod
	def hasNumbers(inputString):
	    # has_digits=bool(re.search(r'\d', inputString))
	    answer = "none"
	    # numbers=["one","two","three","four","five","six","seven","eight","nine","ten","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
	    get_digits={"one": 1, "1" : 1,"two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5,"5": 5, "six": 6,"6": 6, "seven": 7,"7": 7,"eight": 8,"8": 8,"nine": 9,"9": 9,"ten": 10,"10": 10, "none": False}
	    for number in get_digits:
	    	words = inputString.split()
	    	for word in words:
	    		if number == word or number+"+"== word or number+"-" == word:
	    			answer=number
	    			return get_digits[answer]
	    return False

	
	def experience_requirement(self):
		sentences=self.content.split(".")
		# print sentences
		exp_reqs=[]
		
		for sentence in sentences: 
		  	if ("experience" in sentence.lower()):
		  		has_num= JobAd.hasNumbers(JobAd.to_s(sentence))
		  		# print "======================================="
		  		# print sentence
		  		# print "name:{}, exp have:2, exp needed: {}, show job: {}".format(self.title, has_num, 2>=has_num)
		  		if has_num:
		  			exp_reqs.append(has_num)
		  		  			
		print exp_reqs
		if exp_reqs: 
			self.exp_req=min(exp_reqs)
			return exp_reqs
		else:
			self.exp_req=False
			return False
	
	def meets_requirement(self, exp_int):
		if exp_int >= self.experience_requirement():
			return True
		else:
			return False

	# def get_score(self):
	# 	return self.score

	@classmethod
	def filter_by_exp(cls, yrs_exp, job_ads):
		qualified = []
		for job_ad in job_ads:
			if job_ad.meets_requirement(yrs_exp):
				qualified.append(job_ad)
		return qualified


	@classmethod
	def order_by_score(cls, job_ads):
		return sorted(job_ads, key=lambda x: x.score, reverse=True)

	def score_resume(self, resume):
		jd_words = tb(self.content).words
		cv_words = tb(resume).words
		rezscore = 0
		print cv_words
		
		jd_kws = defaultdict(lambda: 0)
		cv_kws = defaultdict(lambda: 0)
		
		#build dictionaries with keyword being key and
		#number of times it's occured as value
		for keyword in Keyword.objects.all():
			if keyword.name.lower() in [x.lower() for x in cv_words]:
				cv_kws[keyword.name]+=1
			if keyword.name in jd_words:
				jd_kws[keyword.name]+=1

		print cv_kws
		print jd_kws

		print "this is jd keys: {}".format(jd_kws.keys())
		for keyword in jd_kws.keys():
			this_score = cv_kws[keyword]*jd_kws[keyword]
			
			# add this keyword to list of matching kywds b/n resume and job desc
			# if this keyword was in both jd and cv
			if this_score > 0:
				self.matching_words.append(keyword)

			rezscore+= this_score

		print "rezscore{}".format(rezscore)
		return rezscore

	def set_qually_rec(self):
		if self.score > 5:
			self.qually_rec = True
		return self



# # indeed_request_url="http://api.indeed.com/ads/apisearch?publisher=9253729351823762&q=software engineer&l=seattle%2C+wa&sort=&radius=&st=&jt=&start={}&limit=1000&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json"
# # APIresponse = requests.get(indeed_request_url).json()['results']
# # test_job_ads=JobAd.make_job_ads_from_api(APIresponse)
# # print test_job_ads
# # print len(test_job_ads)
# # print type(test_job_ads)
# # print type(test_job_ads[0])

# # print dir(test_job_ads[0])
# # print test_job_ads[0].content


