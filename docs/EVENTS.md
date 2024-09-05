# Events (MQTT)

## Event Handler and Emitter

Esta app provee mensajería a través de mqtt y django signals para notificar cambios en entidades de negocio.

### Instalación

```python
# .docker/app/.env (o archivo equivalente)
...
DJANGO_MQTT_HOST=mqtt
DJANGO_MQTT_PORT=1883
DJANGO_MQTT_USER=desarrollo
DJANGO_MQTT_PASS=desarroll0
...
```

```python
# core/settings/base.py (o archivo equivalente)
...
INSTALLED_APPS = [
...
    "sso.apps.EventsConfig",
...
]
```

### TODO

- agregar documentación sobre el uso.
