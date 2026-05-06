from rest_framework.permissions import BasePermission


class IsAdminOrModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in {"admin", "moderator"}


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        return getattr(obj, "user_id", None) == request.user.id or getattr(obj, "author_id", None) == request.user.id
