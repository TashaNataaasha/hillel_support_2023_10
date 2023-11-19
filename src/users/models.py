from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class ActivationKey(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

class User(AbstractUser):
    is_active = models.BooleanField(default=False)