from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SavedJob(models.Model):
	title = models.CharField(max_length=255)
	url = models.TextField()
	snippet = models.TextField()
	key = models.CharField(max_length=255)
	date = models.DateTimeField()
	company = models.CharField(max_length=255)
	location = models.CharField(max_length=255)

	def __unicode__(self):
		return unicode(self.title)

class Keyword(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255)

	def __unicode__(self):
		return unicode(self.name)

class Resume(models.Model):
	name = models.CharField(max_length=255)
	text = models.TextField()

	def __unicode__(self):
		return unicode(self.name)