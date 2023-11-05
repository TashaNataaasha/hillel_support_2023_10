from rest_framework.permissions import BasePermission
from users.constants import Role

class RoleIsSenior(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.SENIOR

    def has_object_permission(self, request, view, obj):
        return request.user.role == Role.SENIOR

class RoleIsJunior(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.JUNIOR

    def has_object_permission(self, request, view, obj):
        return request.user.role == Role.JUNIOR

class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN

    def has_object_permission(self, request, view, obj):
        return request.user.role == Role.ADMIN

class IssueParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user == obj.junior) or (request.user == obj.senior)
