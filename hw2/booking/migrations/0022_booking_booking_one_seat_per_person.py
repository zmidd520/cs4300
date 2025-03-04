# Generated by Django 4.2.11 on 2025-03-01 08:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0021_seat_seat_movie_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(choices=[('Captain America: Brave New World', 'Captain America: Brave New World'), ('The Monkey', 'The Monkey'), ('Dog Man', 'Dog Man')], max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2025, 3, 1, 8, 59, 37, 261738, tzinfo=datetime.timezone.utc))),
                ('seat', models.CharField(choices=[], max_length=10, unique=True, unique_for_date='date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.UniqueConstraint(fields=('movie', 'seat'), name='one_seat_per_person'),
        ),
    ]
