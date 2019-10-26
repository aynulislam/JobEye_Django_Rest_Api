
# Register your models here.
from django.contrib import admin


from .models import JeJob
admin.site.register(JeJob)

from .models import JeJobSkill
admin.site.register(JeJobSkill)

from .models import JeJobAttachment
admin.site.register(JeJobAttachment)