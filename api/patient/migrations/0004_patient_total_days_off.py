# Generated by Django 4.1.7 on 2023-03-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_days_off'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='total_days_off',
            field=models.PositiveIntegerField(default=0),
        ),
    ]