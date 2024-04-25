# Users

Extiende el model de User de Django para incorporar datos provenientes desde el Portal al modelo de User de Django.

```python
from users.models import CustomUser as User
```

en: .docker\app\Dockerfile, hay que copiar a los users desde django_utils

``` sh
... django_utils/app/sso/ sso/
COPY --chown=instalar:instalar django_utils/app/users/ users/
```

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
