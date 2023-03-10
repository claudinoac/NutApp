# Generated by Django 4.1.6 on 2023-02-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
            ],
        ),
    ]
