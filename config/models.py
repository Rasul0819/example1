from django.db import models

# Create your models here.

class Phone(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField()
    description = models.CharField(max_length=300)
