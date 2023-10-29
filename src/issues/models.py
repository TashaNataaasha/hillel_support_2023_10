from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = [
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('default', 'Default'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='default')
    
from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=20)