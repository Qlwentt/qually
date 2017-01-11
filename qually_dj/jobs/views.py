from django.shortcuts import render
from django.http import HttpResponse

from job_ad import JobAd
from qually_dj.api_wrapper import QuallyApiWrapper


# Create your views here.
def index(request):
	job_ads=QuallyApiWrapper.get_job_ads({'search_term': 'software engineer',
						  					'city': 'seattle',
						  					'state': 'WA'})
	return render(request, 'jobs/index.html', {'jobs': job_ads})


def show(request):
	return render(request, 'jobs/show.html')