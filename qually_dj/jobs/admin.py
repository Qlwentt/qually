from django.contrib import admin
try:
    
	from jobs.models import Keyword
	from jobs.models import SavedJob
	from jobs.models import Resume
except ImportError:
	from qually_dj.jobs.models import Keyword
	from qually_dj.jobs.models import SavedJob
	from qually_dj.jobs.models import Resume


# Register your models here.
admin.site.register(Keyword)
admin.site.register(SavedJob)
admin.site.register(Resume)