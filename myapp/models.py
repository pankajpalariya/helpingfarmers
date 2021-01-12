from django.db import models

# Create your models here.
from django.db.models import CharField


class Register(models.Model):
    username = models.CharField(max_length=130, unique=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)