# Generated by Django 5.0.6 on 2024-06-10 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0009_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField()),
                ('date_of_dispatch', models.DateField()),
                ('quantity_single_room', models.PositiveIntegerField()),
                ('quantity_double_room', models.PositiveIntegerField(null=True)),
                ('quantity_multi_room', models.PositiveIntegerField(null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.hotel')),
                ('user_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
