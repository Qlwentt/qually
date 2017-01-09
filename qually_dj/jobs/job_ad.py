from __future__ import unicode_literals

class JobAd(object):
	"""" A job ad from the Indeed API. It has the following properties:
	Attributes:
		id: unique identitfier 		integer
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
		self.id=properties['id']
		self.title=properties.title['title']
		self.snippet=properties.snippet['snippet']
		self.url=properties.url['url']
		self.company=properties.url['company']
		self.location=properties.url['location']
		self.date=properties.date['date']

	@classmethod
	def make_job_ads_from_api(api_json_resp):
		
