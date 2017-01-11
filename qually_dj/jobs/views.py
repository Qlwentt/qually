from django.shortcuts import render
from django.http import HttpResponse

from job_ad import JobAd
from qually_dj.api_wrapper import QuallyApiWrapper

from jobs.forms import SeeJobsForm


# Create your views here.
def index(request):
	
	form_class = SeeJobsForm
	job_ads=QuallyApiWrapper.get_job_ads({'search_term': form_class['job_title'],
						  					'city': form_class['city'],
						  					'state': form_class['state']})
	
	return render(request, 'jobs/index.html', {'jobs': job_ads})


def show(request):
	return render(request, 'jobs/show.html')