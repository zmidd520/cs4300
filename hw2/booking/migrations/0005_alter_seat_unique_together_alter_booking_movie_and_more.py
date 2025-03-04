# Generated by Django 4.2.11 on 2025-02-28 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_seat_seatnum'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='movie',
            field=models.CharField(choices=[(1, 'Captain America: Brave New World'), (2, 'The Monkey')], max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('movie', 'seat')},
        ),
        migrations.RemoveField(
            model_name='seat',
            name='movie',
        ),
    ]
