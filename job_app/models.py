from django.db import models
from buyer_app.models import ScUser
from buyer_app.models import JeBuyer
from general_app.models import JeCategory
from general_app.models import JeSubCategory
from general_app.models import JeJobType
from general_app.models import JeRateUnitType
from general_app.models import JeDurationUnitType
from general_app.models import JeSkill



# Create your models here.

class JeJob(models.Model):
    buyer_id = models.ForeignKey(JeBuyer, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(JeSubCategory, on_delete=models.CASCADE)
    job_type_id = models.ForeignKey(JeJobType, on_delete=models.CASCADE)
    job_tytle = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    duration = models.IntegerField()
    duration_unit_type_id = models.ForeignKey(JeDurationUnitType, on_delete=models.CASCADE)
    rate_from = models.DecimalField(max_digits=10, decimal_places=2)
    rate_to = models.DecimalField(max_digits=10, decimal_places=2)
    rate_unit_type_id = models.ForeignKey(JeRateUnitType, on_delete=models.CASCADE)
    apply_deadline = models.DateTimeField()
    post_date = models.DateTimeField()

    def __str__(self):
        return str(self.buyer_id)

class JeJobSkill(models.Model):
    job_id = models.ForeignKey(JeJob, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(JeSkill, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.job_id)


class JeJobAttachment(models.Model):
    job_id = models.ForeignKey(JeJob, on_delete=models.CASCADE)
    attachment = models.FileField()
    def __str__(self):
        return str(self.job_id)


