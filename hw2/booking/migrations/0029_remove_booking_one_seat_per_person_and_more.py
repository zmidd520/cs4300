# Generated by Django 4.2.11 on 2025-03-02 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0028_alter_booking_date'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='booking',
            name='one_seat_per_person',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 3, 2, 7, 11, 4, 597386, tzinfo=datetime.timezone.utc)),
        ),
    ]
