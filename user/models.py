from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    city = models.CharField(max_length=100, null=True)
    phone_no = models.IntegerField(null=True)
