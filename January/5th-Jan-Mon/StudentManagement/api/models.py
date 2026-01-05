from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll_no=models.IntegerField()
    name = models.CharField(max_length=100)
    age=models.IntegerField()
