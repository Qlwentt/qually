"""qually_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# the rails equivalent of this file is routes.rb
from django.conf.urls import url, include 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from jobs import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^profile/edit/$', views.UpdateProfileView.as_view(), name='update_profile'),
    url(r'^', include('homepage.urls', namespace='homepage')),
    url(r'^jobs/', include('jobs.urls', namespace='jobs')),
    url(r'^get_resume_json/$',views.get_resume_json, name='get_resume'),
    url(r'^favorite_job/$',views.favorite_job, name='favorite_job'),
]
