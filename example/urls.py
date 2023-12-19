from django.urls import path

from example.admin import admin_site

urlpatterns = [
    path("", admin_site.urls),
]
