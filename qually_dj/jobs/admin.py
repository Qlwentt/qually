from django.contrib import admin
from jobs.models import Keyword
from jobs.models import SavedJob
from jobs.models import Resume
# Register your models here.
admin.site.register(Keyword)
admin.site.register(SavedJob)
admin.site.register(Resume)