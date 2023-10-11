from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().owner


class IsOwnerOrManager(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff and request.method in SAFE_METHODS:
            return True
        return request.user == view.get_object().owner
