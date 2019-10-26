from django.db import models
from general_app.models import JeSkill
from worker_app.models import JeWorker


# Create your models here.

class JeQuestion(models.Model):
    skill_id = models.ForeignKey(JeSkill, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer_a = models.CharField(max_length=100)
    answer_b = models.CharField(max_length=100)
    answer_c = models.CharField(max_length=100)
    answer_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)


    def __str__(self):
        return self.skill_id

class JeTest(models.Model):
    user_id = models.ForeignKey(JeWorker, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time =  models.DateTimeField()
    test_marks = models.DecimalField(max_digits=4, decimal_places=2)
    out_of = models.IntegerField()

    def __str__(self):
        return self.worker_id

class JeTestDetails(models.Model):
    test_id = models.ForeignKey(JeTest, on_delete=models.CASCADE)
    question_id = models.ForeignKey(JeQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)

    def __str__(self):
        return self.worker_id




