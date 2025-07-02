from django.db import models

class DB(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()

# Create your models here.
