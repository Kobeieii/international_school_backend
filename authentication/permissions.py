from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        permissions = request.user.get_all_permissions()
        return request.user and "manage_access" in permissions


class HasPermissionCode(BasePermission):
    def has_permission(self, request, view):
        required_perms = getattr(view, "required_permissions", [])
        user_perms = request.user.get_all_permissions()
        return all(perm in user_perms for perm in required_perms)
