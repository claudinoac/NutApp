from rest_framework import serializers
from meal_plan.models import MealPlan, PlannedMeal, Meal


class PlannedMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedMeal
        fields = ['id', 'name', 'meal_type', 'items']


class MealPlanSerializer(serializers.ModelSerializer):
    meals = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MealPlan
        fields = ['id', 'patient', 'comment', 'meals', 'date_created']

    def validate_patient(self, patient):
        if type(patient) == int:
            patient = self.context['account'].patient_set.filter(id=patient).first()
            if not patient:
                raise serializers.ValidationError("Patient does not exist or is not assigned to you.")
        return patient

    def get_meals(self, instance):
        return PlannedMealSerializer(instance.meals, many=True).data


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['patient', 'planned_meal', 'photo', 'items']


class MealListSerializer(serializers.ModelSerializer):
    time_created = serializers.DateTimeField(format="%b %d, %Y, %H:%M")
    planned_meal = PlannedMealSerializer()
    photo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=False)

    class Meta:
        model = Meal
        fields = ['planned_meal', 'status', 'photo', 'items', 'time_created', 'feedback']


class ExpandedMealListSerializer(MealListSerializer):
    patient = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Meal
        fields = ['patient', 'planned_meal', 'status', 'photo', 'items', 'time_created', 'feedback']

    def get_patient(self, instance):
        return {
            "name": instance.patient.user.full_name,
            "id": instance.patient.id
        }


class MealFeedbackSerializer(serializers.Serializer):
    feedback = serializers.CharField(required=True)
    status = serializers.ChoiceField(choices=['approved', 'rejected'], required=True)
