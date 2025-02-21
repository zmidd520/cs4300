from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    releaseDate = models.DateField(default=None)
    duration = models.TimeField()

class Seat(models.Model):
    # choices for seat number
    SEATS = (
        (1, 'A1'),  (2, 'A2'),  (3, 'A3'),  (4, 'A4'),  (5, 'A5'),  (6, 'A6'),  (7, 'A7'),       
        (8, 'B1'),  (9, 'B2'),  (10, 'B3'), (11, 'B4'), (12, 'B5'), (13, 'B6'), (14, 'B7'),   
        (15, 'C1'), (16, 'C2'), (17, 'C3'), (18, 'C4'), (19, 'C5'), (20, 'C6'), (21, 'C7'),   
        (22, 'D1'), (23, 'D2'), (24, 'D3'), (25, 'D4'), (26, 'D5'), (27, 'D6'), (28, 'D7'),   
        (29, 'E1'), (30, 'E2'), (31, 'E3'), (32, 'E4'), (33, 'E5'), (34, 'E6'), (35, 'E7'),
        (36, 'F1'), (37, 'F2'), (38, 'F3'), (39, 'F4'), (40, 'F5'), (41, 'F6'), (42, 'F7')    
    )

    # choices for seat status
    STATUS = (
        ('R', 'Reserved'),
        ('A', 'Available')
    )

    seatNum = models.CharField(max_length=50, choices=SEATS, unique=True)
    status = models.CharField(max_length=50, choices=STATUS)

class Booking(models.Model):
    movie = models.CharField(choices=[movie.title for movie in Movie.objects.all()])
    seat = models.CharField(choices=[seat.seatNum for seat in Seat.objects.all() if seat.status != 'R'])  # only display available seats
    user = models.OneToOneField(User)
    date = models.DateField(default=None)