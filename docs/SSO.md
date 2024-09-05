# Single-Sign On

Esta app provee autenticación utilizando cuenta MiUchile mediante el uso de Upasaporte del Centro Ucampus (que a su vez, utiliza autenticación con el OpenLDAP de la VTI).

El app **SSO** (`_app/sso_`) en este proyecto provee un segundo mecanismo de autenticación para su proyecto. Funciona exponiendo el endpoint `https://<url||ip>/sso/login`, el cual es utilizado para comunicarse con el [**Portal DCC**](https://apps.dcc.uchile.cl/portal).

El flujo de autenticación para las aplicaciones que utilicen esta integración es el siguiente:

```mermaid
sequenceDiagram

Usuario->>Aplicación: ingresa a una aplicación

activate Aplicación
Aplicación->>Aplicación: revisa sesión
Aplicación->>Portal: redirige al Portal, identifica aplicación
deactivate Aplicación

Portal->>Upasaporte: redirige browser, identifica externo
Upasaporte->>Usuario: solicita credenciales Pasaporte Uchile
Usuario->>Upasaporte: ingresa credenciales, hace clic en Ingresar

activate Upasaporte
Upasaporte->>Upasaporte: valida credenciales del usuario
deactivate Upasaporte

alt error credenciales
    Upasaporte->>Usuario: informa error en autenticación
end

Upasaporte->>Portal: ticket

activate Portal
Portal->>Portal: obtiene información del ticket
deactivate Portal

Portal->>Aplicación: redirige browser

activate Aplicación
Aplicación->>Aplicación: autoriza, inicia sesión
deactivate Aplicación

Aplicación->>Usuario: despliega aplicación
```

### Habilitación

Para integrar esta App en proyecto debe solicitar al Área de Tecnologías de Información del DCC <**ati@dcc.uchile.cl**> la creación de su app indicando:

```dotenv
Nombre: (nombre de la app)
Descripción: (descripción corta de la aplicación, será mostrada a los usuarios en el Portal)
Endpoint: https://<url o ip>/sso/login
Responsable: (nombre de la persona responsable del proyecto)
Email: (debe proveer un correo @*.uchile.cl)
Ambiente: (desarrollo, produccion, localhost)
```

### Instalación

```python
# .docker/app/.env (o archivo equivalente)
...
# la app "develop" redirecciona a localhost:8000 por defecto
DJANGO_SSO_APP=develop
DJANGO_SSO_AUTH=True
...
```

```python
# core/settings/base.py (o archivo equivalente)
...
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sso.apps.SsoConfig",
]
...
```

```python
# urls.py (proyecto)
...
from sso.views import login

urlpatterns = [
    path("sso/", include("sso.urls")),
    path("admin/login/", login),
    path("admin/", admin.site.urls),
...
```

## Otros

- La documentación oficial del Portal: <https://github.com/DCC-FCFM-UCHILE/portal/tree/develop/doc>
- Diagramas de Secuencia: <https://mermaid-js.github.io/mermaid/#/sequenceDiagram>
- Actualmente GitHub no soporta el renderizado de mermaid, pero existe esta extensión: <https://github.com/BackMarket/github-mermaid-extension#install> (Chrome, Firefox, Opera)
