from login.controllers import BaseLoggedInController
from rest_framework import permissions, response
from patient.serializers import PatientProfileSerializer


class PatientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'patient'


class BasePatientController(BaseLoggedInController):
    permission_classes = [
        *BaseLoggedInController.permission_classes,
        PatientPermission,
    ]


class PatientProfileController(BasePatientController):
    serializer_class = PatientProfileSerializer

    def get(self, request):
        serializer = self.serializer_class(instance=request.user.patient)
        return response.Response(data=serializer.data)
