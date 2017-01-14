import mechanize
from BeautifulSoup import BeautifulSoup
import urllib2 
import cookielib
import requests
import random
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
job_scan_pw=os.environ.get('JOB_SCAN_PW')

from jobs.job_ad import JobAd

class SkillSpider(object):
	@staticmethod
	def login_to_jobscan:
		cj = cookielib.CookieJar()
		br = mechanize.Browser()

		br.set_cookiejar(cj)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		br.set_handle_equiv(True)
		br.set_handle_redirect(True)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

		user_agents=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
					'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3',
					'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
					'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
					]

		#pick a random user-agent to try to pretend not to be a bot
		br.addheaders = [('user-agent',  random.choice(user_agents)),
		('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

		#log in
		br.open('https://www.jobscan.co/login')
		 
		br.select_form(name='reg')

		br.form['email']= 'quai.wentt@gmail.com'

		br.form['password']= 'qually123'

		br.submit()

	def peform_jobscan(job_desc):
		br.open('https://www.jobscan.co/')
		br.select_form(name='form')
		br.form['cv']= resume
		br.form['jd']= job_desc
		for f in br.forms():
			print f

		# time.sleep(5)

