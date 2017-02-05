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
		self.exp_req= None
		self.qually_rec = False
		# self.keywords = []

	@staticmethod
	def fix_spacing(text):
		  text=re.sub(r'([a-z:.)])([A-Z]|\d)', r'\1 \2', text)
		  text=re.sub(r'([A-Z])(\d)', r'\1 \2', text)
		  
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
				#added this
				job_ad.exp_req = cj.exp_req
				job_ad.keywords = cj.keywords.all().values_list('name', flat=True)
			except CachedJob.DoesNotExist:  
				job_ad.content=job_ad.set_content()
				#added this
				print "I had to set experience required"
				
				job_ad.exp_req=job_ad.set_exp_req()
				print "experience required is : ", job_ad.exp_req
				job_ad.keywords=[]
		return job_ads
	
	def set_content(self):	
	    # self.content=job_ad_text
	    html = urllib2.urlopen(self.url).read()
	    soup = BeautifulSoup(html)
	    job_ad_text = soup.find('span', attrs={'id': 'job_summary'}).text
	    job_ad_text= JobAd.fix_spacing(job_ad_text)
	    print job_ad_text
	    return job_ad_text

	@staticmethod
	def to_s(tb):
		return ('\t' + str(tb))

	@staticmethod
	def hasNumbers(inputString):
	    # has_digits=bool(re.search(r'\d', inputString))
	    answer = None
	    # numbers=["one","two","three","four","five","six","seven","eight","nine","ten","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
	    get_digits={"one": 1, "1" : 1,"two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5,"5": 5, "six": 6,"6": 6, "seven": 7,"7": 7,"eight": 8,"8": 8,"nine": 9,"9": 9,"ten": 10,"10": 10}
	    found_match = re.match(r'(\d)(\s|\W|\d)', inputString)
	    if found_match is not None:
	    	found_match=found_match.group(0)
	    for number in get_digits:
	    	words = inputString.split()
	    	for word in words:
	    		if (number == word or number+"+"== word or number+"-" == word) or (found_match is not None):
	    			answer=number
	    			if answer == None:
	    				answer = found_match
	    			return get_digits[answer]
	    return False

	
	def set_exp_req(self):
		sentences=re.split(r'[.,]', self.content)
		print sentences
		exp_reqs=[]
		print "Job: ", self.title
		print "======================================="
		print "======================================="
		for sentence in sentences: 
		  	if ("experience" in sentence.lower()):
		  		has_num= JobAd.hasNumbers(JobAd.to_s(sentence))
		  		
		  		print '----------------------------------'
		  		print sentence
		  		print "exp have:3, exp needed: {}, show job: {}".format(has_num, 3>=has_num)
		  		if has_num:
		  			exp_reqs.append(has_num)
		  		print '----------------------------------'
		  		  			
		print "Array of experience required: ",exp_reqs
		if exp_reqs: 
			print "experience required: ", min(exp_reqs)
			print "======================================="
			return min(exp_reqs)
		else:
			print "experience required: FALSE"
			print "======================================="
			return False
		

	
	def meets_requirement(self, user_yrs_exp):
		print "I have {} years experience: ".format(user_yrs_exp)
		# print "type: ", type(yrs_exp)
		
		print "job ad experience req: ", self.exp_req

		if user_yrs_exp >= self.exp_req:
			print "returning true--meets requirements"
			return True
		else:
			print "returning false--doesn't meet"
			return False

	# def get_score(self):
	# 	return self.score

	@classmethod
	def filter_by_exp(cls, user_yrs_exp, job_ads):
		qualified = []
		print "I have {} years of experience".format(user_yrs_exp)

		for job_ad in job_ads:
			if job_ad.meets_requirement(user_yrs_exp):
				print "{}, {} was appended with {} years of experience".format(job_ad.title, job_ad.company, job_ad.exp_req)
				qualified.append(job_ad)
		return qualified


	@classmethod
	def order_by_score(cls, job_ads):
		return sorted(job_ads, key=lambda x: x.score, reverse=True)


	def score_resume(self, resume):
		cv_words = tb(resume).words
		rezscore = 0
		cv_kws = []#defaultdict(lambda: 0)
		cj=CachedJob.objects.get(key=self.key)

		#if there are already for the job ad
		if cj.keywords.all():
			# get keywords for resume
			print "I didn't have to look for job ad keywords"
			for keyword in Keyword.objects.all():
				if keyword.name.lower() in [x.lower() for x in cv_words]:
					cv_kws.append(keyword.name)
			
			# get already saved keywords for job ad 
			jd_kws = self.keywords
			
			# print jd_kws
			# print cv_kws
		#you have to get keywords for both resume and job ad
		else:  
			jd_kws=[]

			cv_words = tb(resume).words
			jd_words = tb(self.content).words 
		
		
		#build dictionaries with keyword being key and
		#number of times it's occured as value
			for keyword in Keyword.objects.all():
				if keyword.name.lower() in [x.lower() for x in cv_words]:
					cv_kws.append(keyword.name)
				if keyword.name.lower() in [x.lower() for x in jd_words]: 
					jd_kws.append(keyword.name)
					keyword.cachedjob_set.add(cj) #add this keyword in database for this job ad
			
			print cv_kws
			print jd_kws
			#set keywords for this job ad
			# self.keywords=cv_kws
		#return the number of keywords that occur in both
		self.matching_words = [w for w in cv_kws if w in jd_kws]
		return len(self.matching_words)


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


