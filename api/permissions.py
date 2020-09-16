from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request, which means allowing GET,
        HEAD or OPTIONS request
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        """
        Write permissions are only allowed to the vendor.
        """
        return obj.vendor == request.user
