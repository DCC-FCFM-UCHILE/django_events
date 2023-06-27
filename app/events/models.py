# events/models.py

from django.db import models
from django.conf import settings

from .functions import _get_mqtt_client


class Event(models.Model):
    class Action(models.TextChoices):
        ADDED = "added", "Added"
        MODIFIED = "modified", "Modified"
        DELETED = "deleted", "Deleted"
        UNKNOWN = "unknown", "Unknown"

    entity = models.CharField(max_length=250)
    key = models.CharField(max_length=250, null=True, blank=True)
    action = models.CharField(max_length=10, choices=Action.choices, default=Action.UNKNOWN)

    def __str__(self):
        return f"{self.entity}:{self.key}:{self.action}" if self.key else f"{self.entity}:{self.action}"
