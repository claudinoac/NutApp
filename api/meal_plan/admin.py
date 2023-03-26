from django.contrib import admin
from meal_plan.models import MealPlan, PlannedMeal, Meal


admin.site.register(MealPlan)
admin.site.register(PlannedMeal)
admin.site.register(Meal)
