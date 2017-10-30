from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        # Always allow GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed for the owner
        return obj.owner == request.user
