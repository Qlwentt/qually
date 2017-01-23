from django.contrib import admin

from jobs.models import Keyword
from jobs.models import SavedJob
from jobs.models import Resume
from jobs.models import Profile
from jobs.models import CachedJob



# Register your models here.
admin.site.register(Keyword)
admin.site.register(SavedJob)
admin.site.register(Resume)
admin.site.register(Profile)
admin.site.register(CachedJob)