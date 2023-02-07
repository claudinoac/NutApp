from rest_framework import serializers
from consultation.models import Consultation
from patient.models import Patient
from nutritionist.models import Nutritionist


class ConsultationSerializer(serializers.ModelSerializer):
    date_from = serializers.DateTimeField(format="%b %d, %Y, %I:%M %p")
    date_to = serializers.DateTimeField(format="%b %d, %Y, %I:%M %p")

    class Meta:
        model = Consultation
        fields = "__all__"


class ConsultationPatientSerializer(ConsultationSerializer):
    professional = serializers.SerializerMethodField(read_only=True)

    def get_professional(self, instance):
        professional = getattr(instance, "nutritionist", self.context.get("professional"))
        if professional:
            return {
                "name": str(professional),
                "id": professional.id
            }


class ConsultationProfessionalSerializer(ConsultationSerializer):
    patient = serializers.SerializerMethodField(read_only=True)

    def get_patient(self, instance):
        return {
            "name": str(instance.patient),
            "id": instance.patient.id
        }
