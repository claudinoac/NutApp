from django.db import transaction
from datetime import date
from meal_plan.models import Meal, MealPlan, PlannedMeal
from rest_framework.exceptions import ValidationError


class MealService:
    def review_meal(self, meal, feedback, status):
        with transaction.atomic():
            patient = meal.patient
            meal.feedback = feedback
            meal.status = status
            patient.save()
            meal.save()
        return meal


class MealPlanService:
    def create(self, patient, comment, nutritionist):
        patient = nutritionist.patient_set.filter(id=patient.id).first()
        if not patient:
            raise ValidationError("Patient does not exist or is not assigned to you.")
        return MealPlan.objects.create(patient=patient, comment=comment, nutritionist=nutritionist)

    def create_planned_meal(self, meal_plan, name, meal_type, items):
        return PlannedMeal.objects.create(
            meal_plan=meal_plan, name=name, meal_type=meal_type, items=items
        )
