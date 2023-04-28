from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=100,primary_key=True)
    mobile=models.IntegerField()
    salary=models.FloatField()
    address=models.TextField()
    dept=models.IntegerField()
    