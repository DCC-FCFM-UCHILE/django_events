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

    @staticmethod
    def emitt():
        events = Event.objects.all()
        if events:
            client = _get_mqtt_client()

            entities = {}
            for e in events:
                if e.entity not in entities:
                    entities[e.entity] = {}
                if e.action not in entities[e.entity]:
                    entities[e.entity][e.action] = []
                if e.key:
                    entities[e.entity][e.action].append(e.key)

            for entity, actions in entities.items():
                for action, keys in actions.items():
                    client.publish(
                        settings.MQTT_TOPIC,
                        f"{settings.MQTT_ORIGIN}:{entity}:{'|'.join(keys)}:{action}" if keys else f"{settings.MQTT_ORIGIN}:{entity}",
                    )
            client.disconnect()
            events.delete()
