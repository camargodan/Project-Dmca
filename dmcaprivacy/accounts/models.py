from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_worker = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
