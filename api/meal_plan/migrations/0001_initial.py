# Generated by Django 4.1.7 on 2023-03-26 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('nutritionist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('nutritionist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutritionist.nutritionist')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PlannedMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('morning_snack', 'Morning Snack'), ('lunch', 'Lunch'), ('afternoon_snack', 'Afternoon Snack'), ('dinner', 'Dinner')], max_length=20)),
                ('items', models.JSONField(default=list)),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plan.mealplan')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plan.plannedmeal')),
            ],
        ),
    ]