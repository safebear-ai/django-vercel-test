# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path

from safebear_admin.admin import admin_site

urlpatterns = [
    path("", admin_site.urls),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
