from __future__ import unicode_literals
import unidecode
# _*_ coding:utf-8 _*_
# encoding=utf8  
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

import mechanize
from BeautifulSoup import BeautifulSoup
import urllib2 
import cookielib
import requests
import random
import time
import os


# from jobs.job_ad import JobAd
from jobs.models import Resume
from jobs.models import Keyword
from django.contrib.auth.models import User


class SkillSpider(object):
	@staticmethod
	def login_jobscan():
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
		br.form['email']= os.environ["JOB_SCAN_EMAIL"]
		br.form['password']= os.environ["JOB_SCAN_PW"]
		br.submit()
		return br

	@staticmethod
	def perform_jobscan(br,job_desc):
		br.open('https://www.jobscan.co/')
		br.select_form(name='form')
		br.form['cv']= User.objects.get(username=qlwentt).profile.resume
		br.form['jd']= job_desc
		# for f in br.forms():
		# 	print f
		br.submit()
		return BeautifulSoup(br.response())

	@staticmethod
	def get_keywords(soup):
		# get skills
		skills=soup.findAll("span", attrs={"data-skillkey":True})
		# get categories
		categories = soup.findAll(attrs={"data-skill":True})
		keywords =[]
		
		# get text from html
		for skill in skills:
			keywords.append(skill.getText())
		for cat in categories:
			keywords.append(cat.getText())
			
		# get unique values by chaging it to a set
		keywords = set(keywords)
		print keywords
		return keywords
	
	@staticmethod	
	def add_keywords_to_database(keywords):
		for kyword in keywords:
			try:
				Keyword.objects.get(name=kyword)
			except Keyword.DoesNotExist: 
				Keyword.objects.create(name=kyword, category='none')



