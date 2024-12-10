from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        "fecha_creacion",
        "fecha_modificacion",
    )
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    list_per_page = 250
