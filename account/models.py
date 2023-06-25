from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    email = models.EmailField(unique=True, null=False)
    birthYMD = models.CharField(max_length=6)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'