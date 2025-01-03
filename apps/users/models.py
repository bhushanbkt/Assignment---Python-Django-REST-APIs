from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    college = models.CharField(max_length=100)
    semester = models.IntegerField()
    default_payment_methods = models.CharField(max_length=100, blank=True)
