from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from job_ad import JobAd
from jobs.models import Keyword
from qually_dj.api_wrapper import QuallyApiWrapper
from qually_dj.skill_spider import SkillSpider

from jobs.forms import SeeJobsForm
import json
import time



# Create your views here.
def index(request):
	form = SeeJobsForm(request.GET)
	# left_form = SeeJobsFormLeft(request.GET)
	# right_form = SeeJobsFormRight(request.GET)

	if form.is_valid():
		data=form.cleaned_data
	#have case for if the form is not valid
	
	
	num_records = 25

	user_input={'search_term': data['job_title'],
				'city': data['city'],
				'state': data['state'],
				'resume': data['resume']}
	search_id = json.dumps(user_input, sort_keys=True)

	if search_id in request.session:
		filtered_jobs = request.session.get(search_id)
	else:
		job_ads=[]
		for i in range(num_records/25):
			job_ads.extend(QuallyApiWrapper.get_job_ads(user_input, i*25))
		
		#use job_ads content to get keywords
		
		br = SkillSpider.login_jobscan()
		for job_ad in job_ads:
			soup = SkillSpider.perform_jobscan(br, job_ad.content)
			keywords=SkillSpider.get_keywords(soup)
			SkillSpider.add_keywords_to_database(keywords)
			time.sleep(4)
		
		job_scores = []

		for job_ad in job_ads:
			job_ad.score = job_ad.score_resume(user_input['resume'])

		print "job_scores: {}".format(job_scores)

		#filter by experience--leaving out those that don't match
		filtered_jobs=JobAd.filter_by_exp(form['yrs_exp'], job_ads)
		
		# filtered_jobs=JobAd.filter_by_score
		
		#put this search_id in the session
		request.session[search_id] = filtered_jobs
	
	page = request.GET.get('page')
	paginator = Paginator(filtered_jobs, 10) #show 10 jobs per page

 	try:
 		filtered_jobs = paginator.page(page)
 	except PageNotAnInteger:
 		# If page is not an integer, deliver first page
 		filtered_jobs = paginator.page(1)
 	except EmptyPage:
 		# If page is out of range (e.g. 9999), deliver last page of results
 		filtered_jobs = paginator.page(paginator.num_pages)

	return render(request, 'jobs/index.html', {'jobs': filtered_jobs})


def show(request):
	return render(request, 'jobs/show.html')