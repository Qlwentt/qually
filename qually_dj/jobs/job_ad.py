# _*_ coding:utf-8 _*_
from __future__ import unicode_literals


import sys  
import unidecode
import re

import urllib2
from textblob import TextBlob as tb
from BeautifulSoup import BeautifulSoup
import re
import requests
import unidecode

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
			return min(exp_reqs)
		else:
			return False
	
	def meets_requirement(self, exp_int):
		if exp_int >= self.experience_requirement():
			return True
		else:
			return False

	@classmethod
	def filter_by_exp(cls, yrs_exp, job_ads):
		qualified = []
		for job_ad in job_ads:
			if job_ad.meets_requirement(yrs_exp):
				qualified.append(job_ad)
		return qualified

# # indeed_request_url="http://api.indeed.com/ads/apisearch?publisher=9253729351823762&q=software engineer&l=seattle%2C+wa&sort=&radius=&st=&jt=&start={}&limit=1000&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2&format=json"
# # APIresponse = requests.get(indeed_request_url).json()['results']
# # test_job_ads=JobAd.make_job_ads_from_api(APIresponse)
# # print test_job_ads
# # print len(test_job_ads)
# # print type(test_job_ads)
# # print type(test_job_ads[0])

# # print dir(test_job_ads[0])
# # print test_job_ads[0].content


