# Generated by Django 4.2.11 on 2025-02-28 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_booking_seat_alter_seat_seatnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 28, 23, 5, 56, 627825, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='movie',
            field=models.CharField(choices=[('Captain America: Brave New World', 'Captain America: Brave New World'), ('The Monkey', 'The Monkey'), ('Dog Man', 'Dog Man')], max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('D5', 'D5'), ('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E4'), ('E5', 'E5')], max_length=10, unique=True, unique_for_date=models.DateField(default=datetime.datetime(2025, 2, 28, 23, 5, 56, 627825, tzinfo=datetime.timezone.utc))),
        ),
    ]
