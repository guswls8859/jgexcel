from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)
    count = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
