from login.controllers import BaseLoggedInController
from rest_framework import permissions


class PatientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'patient'


class BasePatientController(BaseLoggedInController):
    permission_classes = [
        *BaseLoggedInController.permission_classes,
        PatientPermission,
    ]
