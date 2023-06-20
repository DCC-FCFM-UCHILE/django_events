# users/admin.py

from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.db import models

from django_json_widget.widgets import JSONEditorWidget

from .models import CustomUser


admin.site.unregister(Group)


class UserInline(admin.StackedInline):
    model = CustomUser.groups.through
    extra = 1


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin):
    list_display = [
        "name",
    ]
    inlines = [UserInline]


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "alias",
        "email",
        "foto_img_tag",
    ]

    def foto_img_tag(self, obj):
        return mark_safe(f'<img loading="lazy" src="{obj.url_foto}" alt="{str(obj.alias)}" height="30px" />')

    foto_img_tag.short_description = "Foto"
    foto_img_tag.allow_tags = True

    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
