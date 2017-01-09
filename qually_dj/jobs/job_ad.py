from __future__ import unicode_literals
import urllib2
from textblob import TextBlob as tb
from BeautifulSoup import BeautifulSoup

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

	@staticmethod
	def fix_spacing(text):
		  return re.sub(r'([a-z:.)])([A-Z])', r'\1 \2', text)


	def __init__(self, properties):
		#Returns job ad object with properties
		self.key=properties['key']
		self.title=properties.title['title']
		self.snippet=properties.snippet['snippet']
		self.content=''
		self.url=properties.url['url']
		self.company=properties.url['company']
		self.location=properties.url['location']
		self.date=properties.date['date']

	@classmethod
	def make_job_ads_from_api(cls,api_json_resp):
		job_ads=[]

		for result in api_json_resp:
			job_ads.append(cls.JobAd({
				'key': result['jobkey'],
				'title': result['jobtitle'],
				'snippet': result['snippet'],
				'url': result['url'],
				'company': result['company'],
				'location': result['formattedLocation'],
				'date': result['date']
				})) 
		return job_ads
	
	def set_content(self):	
	    html = urllib2.urlopen(self.url).read()
	    soup = BeautifulSoup(html)
	    job_ad_text = soup.find('span', attrs={'id': 'job_summary'}).text
	    job_ad_text=fix_spacing(job_ad_text)
	  	self.content=job_ad_text
		return job_ad_text

	



