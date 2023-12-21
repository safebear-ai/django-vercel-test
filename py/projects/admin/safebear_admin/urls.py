from django.urls import path

from safebear_admin.admin import admin_site

urlpatterns = [
    path("", admin_site.urls),
]
