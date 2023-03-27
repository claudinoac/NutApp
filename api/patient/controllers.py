from login.controllers import BaseLoggedInController
from rest_framework import permissions, response, views, generics
from patient.serializers import PatientProfileSerializer, PatientSerializer
from patient.models import Patient
from nutritionist.controllers import BaseNutritionistController


class PatientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'patient'


class BasePatientController(BaseLoggedInController):
    permission_classes = [
        *BaseLoggedInController.permission_classes,
        PatientPermission,
    ]


class PatientProfileController(BasePatientController, views.APIView):
    serializer_class = PatientProfileSerializer

    def get(self, request):
        serializer = self.serializer_class(instance=request.user.patient)
        return response.Response(data=serializer.data)


class PatientController(BaseNutritionistController, generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(nutritionist=self.request.user.nutritionist)
