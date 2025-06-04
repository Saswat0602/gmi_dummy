# user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)  # Ensure unique email addresses
    username = models.CharField(max_length=150, unique=True)  # Ensure unique usernames
    password = models.CharField(max_length=128)  # Password field
    phone = models.CharField(max_length=20, blank=True, null=True)  # Optional phone number
    is_active = models.BooleanField(default=True)  # Active status
    is_superuser = models.BooleanField(default=False)  # Superuser status
    date_joined = models.DateTimeField(auto_now_add=True)  # Date when the user joined
    last_login = models.DateTimeField(auto_now=True,null=True)  # Last login timestamp
    profile_picture = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)  # Optional biography
    role = models.CharField(max_length=100)  # Global role
    region_ids = models.JSONField(default=list)  # List of region IDs
    is_verified = models.BooleanField(default=False)  # Email verification status
