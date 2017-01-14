from django.contrib import admin
from jobs.models import Keyword
from jobs.models import SavedJob
# Register your models here.
admin.site.register(Keyword)
admin.site.register(SavedJob)