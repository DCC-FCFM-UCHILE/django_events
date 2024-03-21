# Users

Extiende el model de User de Django para incorporar datos provenientes desde el Portal al modelo de User de Django.

requierements:

- django-hijack
- django-json-widget

```python
# core/settings/base.py (o archivo equivalente)
...
INSTALLED_APPS = [
...
    "django_json_widget", "hijack", "hijack.contrib.admin",
    "sso.apps.UsersConfig",
...
]

MIDDLEWARE = [
...
    "hijack.middleware.HijackUserMiddleware",
...
]

AUTH_USER_MODEL = "users.CustomUser"
```

```python
# core/urls.py (o archivo equivalente)
urlpatterns = [
    path('hijack/', include('hijack.urls')),
...
]
```


## Otros

- https://testdriven.io/blog/django-custom-user-model/
- https://testdriven.io/blog/django-custom-user-model-migration/