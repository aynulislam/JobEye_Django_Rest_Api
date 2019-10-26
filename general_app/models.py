from django.db import models

# Create your models here.
from django.db import models
from buyer_app.models import ScUser
from buyer_app.models import JeBuyer

from django.db import models


# Create your models here.


class JeCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category)


class JeSubCategory(models.Model):
    categoty_id =  models.ForeignKey(JeCategory, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100)

    def __str__(self):
        return str(self.categoty_id)


class JeJobType(models.Model):
    job_type = models.CharField(max_length=20, )

    def __str__(self):
        return self.job_type


class JeDurationUnitType(models.Model):
    duration_unit_type = models.CharField(max_length=20)

    def __str__(self):
        return self.duration_unit_type


class JeRateUnitType(models.Model):
    rate_unit_type = models.CharField(max_length=20)

    def __str__(self):
        return self.rate_unit_type


class JeSkillType(models.Model):
    skill_type = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_type


class JeSkill(models.Model):
    skill_type_id =  models.ForeignKey(JeSkillType, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_type_id


class JeWorkStatus(models.Model):
    work_status = models.CharField(max_length=100)

    def __str__(self):
        return self.work_status
