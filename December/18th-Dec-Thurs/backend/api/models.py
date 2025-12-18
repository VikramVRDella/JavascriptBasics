from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll_no=models.IntegerField(null=False)
    name=models.CharField(max_length=100,null=False)
    age=models.IntegerField()
