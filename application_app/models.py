from django.db import models
from job_app.models import JeJob
from worker_app.models import JeWorker
from general_app.models import JeWorkStatus
# Create your models here.
class JeJobApplication(models.Model):
    job_id = models.ForeignKey(JeJob, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(JeWorker, on_delete=models.CASCADE)
    description =  models.TextField()
    duration = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    apply_date = models.DateTimeField()

    def __str__(self):
        return self.job_id


class JeJobWorkStatus(models.Model):
    application_id = models.ForeignKey(JeJob, on_delete=models.CASCADE)
    work_status_id = models.ForeignKey(JeWorkStatus, on_delete=models.CASCADE)
    offer_date = models.DateTimeField()
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    ratings = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.application_id

