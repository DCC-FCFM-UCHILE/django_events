# core/settings/docker.py

from core.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]
