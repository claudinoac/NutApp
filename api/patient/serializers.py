from rest_framework import serializers
from patient.models import Patient


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    available_days_off = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'streak_score', 'accumulated_score', 'available_days_off']

    def get_name(self, instance):
        return instance.user.full_name

    def get_available_days_off(self, instance):
        return instance.days_off
