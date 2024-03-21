import threading
from django.apps import AppConfig

from .functions import _mqtt_loop


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self):
        from django.conf import settings
        from core.functions import get_env_variable

        settings.MQTT_HOST = get_env_variable("DJANGO_MQTT_HOST")
        settings.MQTT_PORT = int(get_env_variable("DJANGO_MQTT_PORT"))
        settings.MQTT_USER = get_env_variable("DJANGO_MQTT_USER")
        settings.MQTT_PASS = get_env_variable("DJANGO_MQTT_PASS")
        settings.MQTT_TOPIC = "events"
        settings.MQTT_ORIGIN = "django_utils"

        mqtt_thread = threading.Thread(target=_mqtt_loop)
        mqtt_thread.daemon = True
        mqtt_thread.start()
