from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SavedJob(models.Model):
	title = models.CharField()
	url = models.CharField()
	snippet = models.TextField()
	key = models.CharField()
	date = models.DateTimeField()
	company = models.CharField()
	location = models.CharField()

	def __unicode__(self):
		return self.title