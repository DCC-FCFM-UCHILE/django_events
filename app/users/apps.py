from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        from django.conf import settings

        from core.functions import get_env_variable

        settings.HIJACK_LOGIN_REDIRECT_URL = get_env_variable("USER_HIJACK_LOGIN_VIEW", "admin:index")
