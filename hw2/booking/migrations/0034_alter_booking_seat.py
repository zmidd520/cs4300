# Generated by Django 4.2.11 on 2025-03-03 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0033_booking_booking_one_seat_per_person_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.seat'),
        ),
    ]
