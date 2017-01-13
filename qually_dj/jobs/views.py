from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from job_ad import JobAd
from qually_dj.api_wrapper import QuallyApiWrapper

from jobs.forms import SeeJobsForm


# Create your views here.
def index(request):
	form = SeeJobsForm(request.POST)

	if form.is_valid():
		form=form.cleaned_data
	job_ads=[]
	num_records = 50

	for i in range(num_records/25):
		job_ads.extend(QuallyApiWrapper.get_job_ads({'search_term': form['job_title'],
							  					'city': form['city'],
							  					'state': form['state']}, i*25))
	filtered_jobs=JobAd.filter_by_exp(form['yrs_exp'], job_ads)
	
	page = request.GET.get('page')
	paginator = Paginator(filtered_jobs, 10) #show 10 jobs per page

	# try:
	# 	filtered_jobs = paginator.page(page)
 #    except PageNotAnInteger:
 #        # If page is not an integer, deliver first page.
 #        filtered_jobs = paginator.page(1)
 #    except EmptyPage:
 #        # If page is out of range (e.g. 9999), deliver last page of results.
 #        filtered_jobs = paginator.page(paginator.num_pages)
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