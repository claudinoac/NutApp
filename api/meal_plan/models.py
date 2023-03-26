from django.db import models


class MealPlan(models.Model):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    nutritionist = models.ForeignKey('nutritionist.Nutritionist', on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateField(auto_now_add=True, editable=False)

    @property
    def meals(self):
        return self.plannedmeal_set.all()


class PlannedMeal(models.Model):
    name = models.CharField(max_length=100)
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=(
        ('breakfast', 'Breakfast'),
        ('morning_snack', 'Morning Snack'),
        ('lunch', 'Lunch'),
        ('afternoon_snack', 'Afternoon Snack'),
        ('dinner', 'Dinner')
    ))
    items = models.JSONField(null=False, blank=False)

    def __str__(self):
        return self.name


class Meal(models.Model):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    planned_meal = models.ForeignKey(PlannedMeal, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    items = models.JSONField(null=False, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True)
    status = models.CharField(max_length=20, default="pending_review", choices=(
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending_review', 'Pending Review'),
    ))
