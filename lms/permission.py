from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsManager(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists() and request.method in SAFE_METHODS:
            return True
        return False
