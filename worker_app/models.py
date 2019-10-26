from django.db import models
from buyer_app.models import ScUser
from general_app.models import JeSkill


# Create your models here.

class JeWorker(models.Model):
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=1000)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.user_id


class JeWorkerPortfolio(models.Model):
    worker_id = models.ForeignKey(JeWorker, on_delete=models.CASCADE)
    description = models.TextField()
    link = models.CharField(max_length=1000)
    attachment = models.FileField()
    image = models.FileField()

    def __str__(self):
        return self.worker_id


class JeWorkerSkill(models.Model):
    worker_id = models.ForeignKey(JeWorker, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(JeSkill, on_delete=models.CASCADE)


    def __str__(self):
        return self.worker_id


class JeCertification(models.Model):
    certification = models.CharField(max_length=100)

    def __str__(self):
        return self.worker_id





class JeWorkerCertification(models.Model):
    worker_id = models.ForeignKey(JeWorker, on_delete=models.CASCADE)
    certification_id = models.ForeignKey(JeCertification, on_delete=models.CASCADE)


    def __str__(self):
        return self.worker_id


