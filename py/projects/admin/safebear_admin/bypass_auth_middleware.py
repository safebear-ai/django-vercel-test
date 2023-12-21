from django.contrib.auth.models import AnonymousUser


class MockAdminUser(AnonymousUser):
    id = None
    pk = None
    is_staff = True
    is_active = True
    is_superuser = True

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class BypassAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = MockAdminUser()
        return self.get_response(request)
