from django.contrib import admin

# Register your models here.

from .models import JeJobApplication
admin.site.register(JeJobApplication)

from .models import JeJobWorkStatus
admin.site.register(JeJobWorkStatus)

