# Generated by Django 4.1.7 on 2023-03-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan', '0002_alter_plannedmeal_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='meal',
            new_name='planned_meal',
        ),
        migrations.AddField(
            model_name='meal',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]