# Users

Extiende el model de User de Django para incorporar data proveniente desde el Portal al modelo de User de Django.



```python
# settings.py (proyecto)
...
INSTALLED_APPS = [
...
    "sso.apps.UsersConfig",
...
]

AUTH_USER_MODEL = "users.CustomUser"
```


## Otros

- https://testdriven.io/blog/django-custom-user-model/
- https://testdriven.io/blog/django-custom-user-model-migration/