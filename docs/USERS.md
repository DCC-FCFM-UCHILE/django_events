# Users

Extiende el model de User de Django para incorporar data proveniente desde el Portal al modelo de User de Django.

requierements:

- django-hijack
- django-json-widget

```python
# settings.py (proyecto)
...
INSTALLED_APPS = [
...
    "hijack",
    "django_json_widget",
    "sso.apps.UsersConfig",
...
]

MIDDLEWARE = [
...
    "hijack.middleware.HijackUserMiddleware",
...
]

AUTH_USER_MODEL = "users.CustomUser"
HIJACK_LOGIN_REDIRECT_URL = "admin:index"
```


```python
# urls.py
from django.urls import include, path


urlpatterns = [
    path('hijack/', include('hijack.urls')),
    # …
]
```


## Otros

- https://testdriven.io/blog/django-custom-user-model/
- https://testdriven.io/blog/django-custom-user-model-migration/