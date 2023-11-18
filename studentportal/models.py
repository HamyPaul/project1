from django.db import models

class student(models.Model):
    Admission_No=models.IntegerField()
    Name=models.CharField(max_length=100,default=None)
    Age= models.IntegerField(default=None)
    Phone_no=models.IntegerField(default=None)
    
