from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    last = models.CharField(max_length=30)
    first = models.CharField(max_length=25)
