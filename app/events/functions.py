# events/functions.py

from django.conf import settings

from .mqtt import emitter_event_signal, get_mqtt_client


# se debe importar para emitir eventos
def emitt_event(entity, key=None, action=None):
    return emitter_event_signal.send(sender="APP", origin=settings.MQTT_ORIGIN, entity=entity, key=key, action=action)


# crea un loop de conexión a la cola
def mqtt_loop():
    client = get_mqtt_client()
    client.loop_forever()
