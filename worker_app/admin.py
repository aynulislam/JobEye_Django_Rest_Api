from django.contrib import admin

# Register your models here.


from .models import  JeWorker
admin.site.register(JeWorker)

from .models import JeWorkerPortfolio
admin.site.register(JeWorkerPortfolio)


from .models import JeWorkerSkill
admin.site.register(JeWorkerSkill)

from .models import JeWorkerCertification
admin.site.register(JeWorkerCertification)

from .models import JeCertification
admin.site.register(JeCertification)





