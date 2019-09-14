from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    pvt_key = models.CharField(max_length=100)