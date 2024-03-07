from django.db import models

class Service(models.Model):
    # here we keep fields
    service_icon=models.CharField(max_length=50) # in CharField  (max_length=) is necessary
    service_title=models.CharField(max_length=50)
    service_des = models.TextField()

# Create your models here.
