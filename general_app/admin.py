


from django.contrib import admin


from .models import  JeCategory
admin.site.register(JeCategory)

from .models import JeSubCategory
admin.site.register(JeSubCategory)


from .models import JeJobType
admin.site.register(JeJobType)

from .models import JeDurationUnitType
admin.site.register(JeDurationUnitType)

from .models import JeRateUnitType
admin.site.register(JeRateUnitType)


from .models import JeSkill
admin.site.register(JeSkill)

from .models import JeSkillType
admin.site.register(JeSkillType)


from .models import JeWorkStatus
admin.site.register(JeWorkStatus)

