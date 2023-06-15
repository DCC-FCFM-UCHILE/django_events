## Event Handler and Emitter

Esta app provee mensajería a través de mqtt y django signals para notificar cambios en entidades de negocio.

### Instalación

```python
# .env (proyecto)
...
DJANGO_MQTT_HOST=mqtt
DJANGO_MQTT_PORT=1883
DJANGO_MQTT_USER=desarrollo
DJANGO_MQTT_PASS=desarroll0
...
```

```python
# settings.py (proyecto)
...
INSTALLED_APPS = [
...
    "sso.apps.EventsConfig",
...
]
...
MQTT_HOST = get_env_variable("DJANGO_MQTT_HOST")
MQTT_PORT = int(get_env_variable("DJANGO_MQTT_PORT"))
MQTT_USER = get_env_variable("DJANGO_MQTT_USER")
MQTT_PASS = get_env_variable("DJANGO_MQTT_PASS")
MQTT_TOPIC = "events"
MQTT_ORIGIN = "django_utils"
...
```

# TODO

- agregar documentación sobre el uso.
