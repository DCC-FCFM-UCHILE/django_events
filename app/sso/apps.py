from django.apps import AppConfig


class SsoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sso"

    def ready(self):
        from django.conf import settings
        from core.functions import get_env_variable

        settings.LOGIN_URL = "sso:index"
        settings.SSO_URL = "https://portal.dcc.uchile.cl"
        settings.SSO_APP = get_env_variable("DJANGO_SSO_APP")
        settings.SSO_AUTH = get_env_variable("DJANGO_SSO_AUTH")
