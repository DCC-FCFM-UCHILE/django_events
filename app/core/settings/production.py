# core/settings/production.py

from core.settings.base import *


DEBUG = False

ALLOWED_HOSTS = [
    "api.apps.dcc.uchile.cl",
    "api.test.dcc.uchile.cl",
    "api.dev.dcc.uchile.cl",
    "pad_feriados:8000",
]

CSRF_TRUSTED_ORIGINS = [
    "https://api.apps.dcc.uchile.cl",
    "https://api.test.dcc.uchile.cl",
    "https://api.dev.dcc.uchile.cl",
    "http://pad_feriados:8000",
]

ADMINS = [
    ("Área de Desarrollo de Software", "desarrollo@dcc.uchile.cl"),
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
}
