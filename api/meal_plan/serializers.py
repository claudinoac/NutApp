from rest_framework import serializers
from meal_plan.models import MealPlan, PlannedMeal, Meal


class PlannedMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedMeal
        fields = ['id', 'name', 'meal_type', 'items']


class MealPlanSerializer(serializers.ModelSerializer):
    meals = serializers.ListSerializer(child=PlannedMealSerializer(), read_only=True)

    class Meta:
        model = MealPlan
        fields = ['id', 'patient', 'comment', 'meals', 'date_created']

    def validate_patient(self, patient):
        if type(patient) == int:
            patient = self.context['account'].patient_set.filter(id=patient).first()
            if not patient:
                raise serializers.ValidationError("Patient does not exist or is not assigned to you.")
        return patient


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['patient', 'planned_meal', 'photo', 'items']
