from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("hijack/", include("hijack.urls")),
    path("admin/", admin.site.urls),
    path("sso/", include("sso.urls")),
]
