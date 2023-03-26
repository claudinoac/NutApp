from login.controllers import BaseLoggedInController
from rest_framework import permissions


class NutritionistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'nutritionist'


class BaseNutritionistController(BaseLoggedInController):
    permission_classes = [
        *BaseLoggedInController.permission_classes,
        NutritionistPermission,
    ]
