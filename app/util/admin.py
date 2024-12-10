from django.contrib import admin

from common.admin import BaseModelAdmin

from .models import Parametro, Texto


@admin.register(Texto)
class TextoAdmin(BaseModelAdmin):
    list_display = (
        "identificador",
        "fecha_creacion",
        "fecha_modificacion",
    )
    ordering = (
        "identificador",
    )


@admin.register(Parametro)
class ParametroAdmin(BaseModelAdmin):
    list_display = (
        "identificador",
        "nombre",
        "valor",
        "tipo",
        "fecha_modificacion",
    )
    ordering = (
        "identificador",
    )
