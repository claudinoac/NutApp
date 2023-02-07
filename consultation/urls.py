from consultation.controllers import ConsultationNutritionistController, ConsultationPatientController
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"nutritionist", ConsultationNutritionistController, basename="nutritionist")
router.register(r"patient", ConsultationPatientController, basename="patient")

urlpatterns = router.urls
