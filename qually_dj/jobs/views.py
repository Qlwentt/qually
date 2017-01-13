from django.shortcuts import render
from django.http import HttpResponse

from job_ad import JobAd
from qually_dj.api_wrapper import QuallyApiWrapper

from jobs.forms import SeeJobsForm


# Create your views here.
def index(request):
	form = SeeJobsForm(request.POST)

	if form.is_valid():
		form=form.cleaned_data

		job_ads=QuallyApiWrapper.get_job_ads({'search_term': form['job_title'],
							  					'city': form['city'],
							  					'state': form['state']})
		filtered_jobs=JobAd.filter_by_exp(form['yrs_exp'], job_ads)
	
	return render(request, 'jobs/index.html', {'jobs': filtered_jobs})


def show(request):
	return render(request, 'jobs/show.html')