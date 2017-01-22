from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages




from job_ad import JobAd
from jobs.models import Keyword, User, Profile
from qually_dj.api_wrapper import QuallyApiWrapper
from qually_dj.skill_spider import SkillSpider
from jobs.forms import UserForm, ProfileForm, SignUpForm

from jobs.forms import SeeJobsForm
import json
import time

class SignUpView(FormView):
    template_name = 'registration/signup.html'

    def get(self, request):
        signup_form = SignUpForm()
        return render(request, self.template_name, {'signup_form': signup_form})

    def post(self, request):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, ('Your account was successfully created!'))
            new_user = authenticate(username=signup_form.cleaned_data['username'], password=signup_form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('/profile/edit')
        else:
            messages.error(request, ('There is something not quite right...'))
            return render(request, self.template_name, {'signup_form': signup_form})

# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'profiles/profile.html'
#     def get(self, request, pk):
#         profile = get_object_or_404(Profile, pk=pk)


class UpdateProfileView(LoginRequiredMixin, FormView):
    template_name = 'profiles/update_profile.html'

    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        print request.user
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
            # 'saved_jobs': request.user.jobs.all()
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/')
        else:
            messages.error(request, ('There is something not quite right...'))
            return render(request, self.template_name, {
                'user_form': user_form,
                'profile_form': profile_form
            })

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
			job_ad.set_qually_rec()
			print job_ad.qually_rec
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