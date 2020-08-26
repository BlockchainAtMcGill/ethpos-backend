from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the author of a post
        return obj.vendor == request.user