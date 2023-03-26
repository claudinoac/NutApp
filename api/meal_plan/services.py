from django.db import transaction


class MealService:
    def review_meal(self, meal, feedback, status):
        with transaction.atomic():
            patient = meal.patient
            meal.feedback = feedback
            meal.status = status
            if meal.status == 'approved':
                patient.streak_points += 1
                patient.points += 1
            else:
                patient.streak_points = 0
                patient.points = 0
            patient.save()
            meal.save()
        return meal
