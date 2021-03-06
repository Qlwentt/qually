from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.


class Keyword(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255, blank=True)

	def __unicode__(self):
		return unicode(self.name)

class Resume(models.Model):
	name = models.CharField(max_length=255)
	text = models.TextField()
	def __unicode__(self):
		return unicode(self.name)

class CachedJob(models.Model):
	keywords = models.ManyToManyField(Keyword, blank=True)
	
	key = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	url = models.TextField()
	snippet = models.TextField()
	content = models.TextField()
	exp_req = models.IntegerField(default=0)


	def __unicode__(self):
		return unicode(self.title)

class SavedJob(models.Model):
	cached_job = models.ForeignKey(CachedJob, on_delete=models.CASCADE, default=1)
	key = models.CharField(max_length=255)
	date = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	score = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return unicode(self.cached_job.title)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(SavedJob, blank=True)

    # last_name = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    yrs_exp = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100, blank=True)
    resume = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()