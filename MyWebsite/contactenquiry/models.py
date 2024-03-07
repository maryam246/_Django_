from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=50)
    websitelink=models.CharField(max_length=70)
    message=models.TextField()