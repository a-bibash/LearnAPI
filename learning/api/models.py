from django.db import models
from . import *
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
