from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('gso', 'GSO Office'),
        ('unit_head', 'Unit Head'),
        ('personnel', 'Personnel'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    unit = models.CharField(max_length=50, blank=True, null=True)
