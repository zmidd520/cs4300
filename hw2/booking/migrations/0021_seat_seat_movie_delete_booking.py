# Generated by Django 4.2.11 on 2025-03-01 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_alter_booking_date_alter_booking_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='seat_movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.movie'),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
