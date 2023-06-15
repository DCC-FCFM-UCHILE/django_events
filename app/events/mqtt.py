# events/mqtt.py

from django.dispatch import Signal, receiver
from django.conf import settings

import paho.mqtt.client as mqtt

# emitter_event_signal se debe disparar cuando se quiera colocar un mensaje en la cola de events
emitter_event_signal = Signal()
# handler_event_signal se dispara cuando se recibe un mensaje por la cola de events
handler_event_signal = Signal()


def get_mqtt_client() -> mqtt.Client:
    def on_connect(client, userdata, flags, rc):
        print("MQTT Connected: " + str(rc))
        client.subscribe(settings.MQTT_TOPIC)

    # recibe eventos de la cola y dispara handler_event_signal
    def handler_event_signal_fn(client, userdata, msg):
        try:
            data = str(msg.payload).split(":")
            origin = data[0]
            entity = data[1]
            key = data[2] if len(data) >= 3 else None
            action = data[3] if len(data) == 4 else None

            handler_event_signal.send(sender="MQTT", origin=origin, entity=entity, key=key, action=action)
            print(msg.topic + " " + str(msg.payload))
        except Exception:
            print("MENSAJE INCONSISTENTE: " + str(msg.payload))

    def on_publish(client, userdata, mid):
        print("- mensaje publicado con éxito.")

    client = mqtt.Client()
    client.on_publish = on_publish
    client.on_connect = on_connect
    client.on_message = handler_event_signal_fn
    client.username_pw_set(settings.MQTT_USER, password=settings.MQTT_PASS)
    client.connect(host=settings.MQTT_HOST, port=int(settings.MQTT_PORT))
    return client


# recibe eventos emitidos por la app que deben ponerse en la cola
@receiver(emitter_event_signal)
def emitter_event_signal_fn(sender, **kwargs):
    msg = f"{kwargs['origin']}:{kwargs['entity']}"
    if kwargs["key"] is not None and kwargs["key"] != "":
        msg += f":{kwargs['key']}"
        if kwargs["action"] is not None and kwargs["action"] != "" and kwargs["action"] in ["added", "modified", "deleted", "unknown"]:
            msg += f":{kwargs['action']}"

    client = get_mqtt_client()
    client.publish(settings.MQTT_TOPIC, msg)
    client.disconnect()
