from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True , blank = True)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField(max_length = 10)
