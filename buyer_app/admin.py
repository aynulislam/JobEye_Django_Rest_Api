

# Register your models here.
from django.contrib import admin

from .models import ScUser,JeBuyer

admin.site.register(JeBuyer)
admin.site.register(ScUser)