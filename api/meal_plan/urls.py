from django.urls import path
from meal_plan import controllers

urlpatterns = [
    path('meal_plan/', controllers.MealPlanController.as_view()),
    path('meal_plan/<int:plan_id>', controllers.MealPlanController.as_view()),
    path('meal_plan/<int:plan_id>/meals', controllers.PlannedMealController.as_view()),
    path('meals', controllers.MealController.as_view()),
]
