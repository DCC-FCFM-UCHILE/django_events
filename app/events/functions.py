# events/functions.py

import logging

from django.conf import settings

import paho.mqtt.client as mqtt

from .signals import handler_event_signal, emitter_event_signal


logger = logging.getLogger("django")


def _get_from_payload(payload):
    data = "".join(map(chr, payload)).split(":")
    try:
        return {
            "origin": data[0],
            "entity": data[1],
            "key": data[2] if len(data) >= 3 else None,
            "action": data[3] if len(data) == 4 else None,
        }
    except Exception:
        logger.warn("MQTT ERROR mensaje recibido: " + str(payload))
        return {"origin": None, "entity": None, "key": None, "action": None}


def _get_mqtt_client() -> mqtt.Client:
    def on_connect(client, userdata, flags, rc):
        client.subscribe(settings.MQTT_TOPIC)

    # recibe eventos de la cola y dispara handler_event_signal
    def handler_event_signal_fn(client, userdata, msg):
        handler_event_signal.send(sender="MQTT", data=_get_from_payload(msg.payload))

    def on_publish(client, userdata, mid):
        logger.info("MQTT: mensaje publicado con éxito.")

    client = mqtt.Client()
    client.on_publish = on_publish
    client.on_connect = on_connect
    client.on_message = handler_event_signal_fn
    client.username_pw_set(settings.MQTT_USER, password=settings.MQTT_PASS)
    client.connect(host=settings.MQTT_HOST, port=int(settings.MQTT_PORT))
    return client


# recibe eventos emitidos por la app que deben ponerse en la cola
def _emitter_event_signal_fn(sender, **kwargs):
    msg = f"{kwargs['origin']}:{kwargs['entity']}"
    if kwargs["key"] is not None and kwargs["key"] != "":
        msg += f":{kwargs['key']}"
        if kwargs["action"] is not None and kwargs["action"] != "" and kwargs["action"] in ["added", "modified", "deleted", "unknown"]:
            msg += f":{kwargs['action']}"

    client = _get_mqtt_client()
    client.publish(settings.MQTT_TOPIC, msg)
    client.disconnect()


# crea un loop de conexión a la cola
def _mqtt_loop():
    client = _get_mqtt_client()
    client.loop_forever()


# se debe importar para emitir eventos
def emitt_event(entity, key=None, action=None):
    return emitter_event_signal.send(sender="APP", origin=settings.MQTT_ORIGIN, entity=entity, key=key, action=action)
