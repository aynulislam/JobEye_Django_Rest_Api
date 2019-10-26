from django.db import models


# Create your models here.
class ScUser(models.Model):
    user_code = models.CharField(max_length=10, unique=True)
    user_name = models.CharField(max_length=100, null=False)
    user_node = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100,null=True )
    password = models.CharField(max_length=255,null=True)
    voice = models.FileField(null=True)
    face = models.FileField(null=True)
    salt = models.IntegerField()
    pin =  models.CharField(max_length=255)

    def __str__(self):
        return self.user_code


class JeBuyer(models.Model):
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=100,)
    longitude =  models.DecimalField(max_digits=10, decimal_places=3)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.user_id

