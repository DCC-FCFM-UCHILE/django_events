import threading
from django.apps import AppConfig

from events.functions import _mqtt_loop
from .functions import _emitter_event_signal_fn
from .signals import emitter_event_signal


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self):
        emitter_event_signal.connect(_emitter_event_signal_fn)

        mqtt_thread = threading.Thread(target=_mqtt_loop)
        mqtt_thread.daemon = True
        mqtt_thread.start()
