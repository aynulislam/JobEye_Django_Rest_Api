from django.contrib import admin

# Register your models here.
from django.contrib import admin


from .models import  JeQuestion
admin.site.register(JeQuestion)

from .models import JeTest
admin.site.register(JeTest)


from .models import JeTestDetails
admin.site.register(JeTestDetails)

