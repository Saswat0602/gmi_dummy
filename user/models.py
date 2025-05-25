# user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    role = models.CharField(max_length=100)  # Global role
    region_ids = models.JSONField(default=list)  # List of region IDs
    is_verified = models.BooleanField(default=False)  # Email verification status
