from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Allow safe methods for any authenticated user, write methods only for owner.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # assume model has created_by
        return getattr(obj, 'created_by', None) == request.user
