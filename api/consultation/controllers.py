from consultation.models import Consultation
from consultation.serializers import ConsultationPatientSerializer, ConsultationProfessionalSerializer
from rest_framework import viewsets, permissions, status, response
from consultation.services import ConsultationService, ConsultationError
from login.controllers import BaseLoggedInController


class ConsultationNutritionistController(BaseLoggedInController, viewsets.ModelViewSet):
    serializer_class = ConsultationProfessionalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Consultation.objects.filter(professional=self.request.user.nutritionist)


class ConsultationPatientController(BaseLoggedInController, viewsets.ModelViewSet):
    serializer_class = ConsultationPatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Consultation.objects.filter(patient=self.request.user.patient)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        consultation_service = ConsultationService()
        try:
            new_consultation = consultation_service.create_consultation(
                patient=request.user.patient,
                professional=request.user.patient.nutritionist,
                date_from=serializer.validated_data["date_from"],
                date_to=serializer.validated_data["date_to"]
            )
        except ConsultationError as consultation_error:
            return response.Response(data=consultation_error.args[0], status=status.HTTP_400_BAD_REQUEST)
        return response.Response(
            data=self.serializer_class(
                instance=new_consultation,
                context={"professional": new_consultation.professional}
            ).data
        )
