from patient.controllers import PatientController, PatientProfileController
from django.urls import path

urlpatterns = [
    path('patients', PatientController.as_view()),
    path('patient/profile', PatientProfileController.as_view()),
]
