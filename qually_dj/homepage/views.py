from django.shortcuts import render
from django.http import HttpResponse
from jobs.forms import SeeJobsForm 
from django.conf.urls import include, url

# Create your views here.
def index(request):
	form_class = SeeJobsForm
	return render(request, 'homepage/index.html', {'form': form_class})