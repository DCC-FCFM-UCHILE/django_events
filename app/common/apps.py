from django.apps import AppConfig
from django.contrib.staticfiles.finders import AppDirectoriesFinder
from django.contrib.staticfiles.storage import staticfiles_storage


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "common"

    def ready(self):

        AppDirectoriesFinder.storages[self.name] = staticfiles_storage