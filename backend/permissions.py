from rest_framework import permissℹons


class IsAuthorOrReadOnly(permissions.BasePermission):
    """"""

    def has_permission(self, request, view):
        # only authenticated users can se list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """REturn `True if permission is granted, `False` otherwise"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user
