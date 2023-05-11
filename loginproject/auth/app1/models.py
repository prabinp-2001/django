from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class auth(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=25)
    

class CustomUser(AbstractUser):
    email=models.EmailField()
    phno=models.IntegerField()
    address=models.CharField(max_length=20)


class Employee(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=25)
    salary=models.IntegerField()

