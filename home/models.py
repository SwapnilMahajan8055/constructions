from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=100)
    massage = models.CharField(max_length=100)