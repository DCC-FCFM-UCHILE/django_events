import threading
from django.apps import AppConfig

from events.functions import mqtt_loop


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self):
        mqtt_thread = threading.Thread(target=mqtt_loop)
        # Para que el hilo se detenga cuando se detenga el programa principal
        mqtt_thread.daemon = True
        mqtt_thread.start()
