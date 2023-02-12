# Generated by Django 4.1.6 on 2023-02-12 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultation', '0001_initial'),
        ('patient', '0001_initial'),
        ('nutritionist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='professional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nutritionist.nutritionist'),
        ),
    ]
