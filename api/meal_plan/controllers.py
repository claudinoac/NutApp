from nutritionist.controllers import BaseNutritionistController
from patient.controllers import BasePatientController
from rest_framework import views, response, status, generics
from meal_plan.serializers import (
    MealPlanSerializer, PlannedMealSerializer, MealSerializer,
    MealListSerializer, MealFeedbackSerializer, ExpandedMealListSerializer
)
from meal_plan.models import MealPlan, PlannedMeal, Meal
from meal_plan.services import MealService
from django.shortcuts import get_object_or_404
from django.http import Http404


class MealPlanController(BaseNutritionistController, views.APIView):
    serializer_class = MealPlanSerializer

    def get(self, request, plan_id):
        meal_plan = get_object_or_404(MealPlan, id=plan_id, nutritionist=request.user.nutritionist)
        serializer = self.serializer_class(instance=meal_plan)
        return response.Response(data=serializer.data)

    def post(self, request):
        nutritionist = request.user.nutritionist
        serializer = self.serializer_class(
            data=request.data, context={'account': nutritionist}
        )
        if not serializer.is_valid():
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        new_meal_plan = MealPlan.objects.create(**serializer.validated_data, nutritionist=nutritionist)
        return response.Response(
            data=self.serializer_class(instance=new_meal_plan).data,
            status=status.HTTP_201_CREATED
        )


class PatientMealPlanController(BasePatientController, views.APIView):
    serializer_class = MealPlanSerializer

    def get(self, request, plan_id=None):
        if plan_id:
            meal_plan = MealPlan.objects.filter(id=plan_id, patient=request.user.patient).first()
        else:
            meal_plan = MealPlan.objects.filter(patient=request.user.patient).last()
        if not meal_plan:
            raise Http404
        return response.Response(data=self.serializer_class(instance=meal_plan).data)


class PlannedMealController(BaseNutritionistController, views.APIView):
    serializer_class = PlannedMealSerializer

    def get(self, request, plan_id):
        meal_plan = get_object_or_404(
            MealPlan, id=plan_id, nutritionist=request.user.nutritionist
        )
        serializer = self.serializer_class(
            instance=meal_plan.plannedmeal_set.all(), many=True
        )
        return response.Response(data=serializer.data)

    def post(self, request, plan_id):
        meal_plan = get_object_or_404(
            MealPlan, id=plan_id, nutritionist=request.user.nutritionist
        )
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        new_planned_meal = PlannedMeal.objects.create(**serializer.validated_data, meal_plan=meal_plan)
        return response.Response(
            data=self.serializer_class(instance=new_planned_meal).data,
            status=status.HTTP_201_CREATED
        )


class MealController(BasePatientController, generics.ListAPIView):
    write_serializer_class = MealSerializer
    serializer_class = MealListSerializer

    def post(self, request):
        serializer = self.write_serializer_class(data={
            **request.data, "patient": request.user.patient.id,
            "status": "pending_review"
        })
        if not serializer.is_valid():
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        new_meal = serializer.save()
        return response.Response(
            data=self.serializer_class(instance=new_meal).data,
            status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        return Meal.objects.filter(patient=self.request.user.patient).order_by('-time_created')


class PatientsMealController(BaseNutritionistController, generics.ListAPIView):
    serializer_class = ExpandedMealListSerializer

    def get_queryset(self):
        return Meal.objects.filter(patient__nutritionist=self.request.user.nutritionist)


class MealFeedbackController(BaseNutritionistController, generics.ListAPIView):
    serializer_class = MealFeedbackSerializer

    def put(self, request, meal_id):
        meal = get_object_or_404(Meal, id=meal_id, patient__nutritionist=request.user.nutritionist)
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        meal_service = MealService()
        updated_meal = meal_service.review_meal(
            meal,
            serializer.validated_data['feedback'],
            serializer.validated_data['status']
        )
        return response.Response(data=MealSerializer(instance=updated_meal).data)
