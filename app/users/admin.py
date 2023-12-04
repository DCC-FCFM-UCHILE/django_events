from hijack.contrib.admin import HijackUserAdminMixin
from django_json_widget.widgets import JSONEditorWidget

from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.shortcuts import resolve_url


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
class CustomUserAdmin(HijackUserAdminMixin, UserAdmin):
    list_display = [
        "username",
        "alias",
        "email",
        "foto_img_tag",
        # "hijack_button",
    ]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Portal DCC"), {"fields": ("alias", "url_foto", "data")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    readonly_fields = (
        "last_login",
        "date_joined",
        "alias",
        "url_foto",
        "data",
    )

    def foto_img_tag(self, obj):
        if obj.url_foto:
            return mark_safe(f'<img loading="lazy" src="{obj.url_foto}" alt="{str(obj.alias)}" height="30px" />')
        return mark_safe('<img loading="lazy" src="https://dcc.uchile.cl/static/images/personas/avatar.png" height="30px" />')

    foto_img_tag.short_description = "Foto"
    foto_img_tag.allow_tags = True

    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    def get_hijack_success_url(self, request, obj):
        return resolve_url(settings.HIJACK_LOGIN_REDIRECT_URL)
