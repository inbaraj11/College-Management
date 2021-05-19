from rest_framework import permissions
from rest_framework.response import Response


# class IsOwnerOrReadOnly(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # if request.user.is_superuser or request.user.is_staff:
        # return obj.user == request.user


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsStaffUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsStudentUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_active