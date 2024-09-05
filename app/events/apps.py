import threading

from django.apps import AppConfig

from .functions import _mqtt_loop


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self):
        mqtt_thread = threading.Thread(target=_mqtt_loop)
        mqtt_thread.daemon = True
        mqtt_thread.start()
