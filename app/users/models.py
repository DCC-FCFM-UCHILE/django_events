# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    url_foto = models.URLField(max_length=250, null=True, blank=True)
    alias = models.CharField(max_length=250)

    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} | {self.first_name} {self.last_name}"
