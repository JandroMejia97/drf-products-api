from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj

    def has_permission(self, request, view):
        return bool(
            request.user 
            and request.user.is_authenticated
            or request.method == 'POST'
        )


class IsSuperuserOrOwner(IsOwner):

    def has_permission(self, request, view):
        return bool(
            request.user 
            and request.user.is_authenticated
            and (
                request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
            )
        )