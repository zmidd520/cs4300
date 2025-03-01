from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    releaseDate = models.DateField(default=None)
    duration = models.TimeField()

class Seat(models.Model):
    # choices for seat number
    SEATS = (
        ('A1', 'A1'),  ('A2', 'A2'),  ('A3', 'A3'),  ('A4', 'A4'),  ('A5', 'A5'),        
        ('B1', 'B1'),  ('B2', 'B2'),  ('B3', 'B3'),  ('B4', 'B4'),  ('B5', 'B5'), 
        ('C1', 'C1'),  ('C2', 'C2'),  ('C3', 'C3'),  ('C4', 'C4'),  ('C5', 'C5'),    
        ('D1', 'D1'),  ('D2', 'D2'),  ('D3', 'D3'),  ('D4', 'D4'),  ('D5', 'D5'),   
        ('E1', 'E1'),  ('E2', 'E2'),  ('E3', 'E3'),  ('E4', 'E4'),  ('E5', 'E5')  
    )

    # choices for seat status
    STATUS = (
        ('R', 'Reserved'),
        ('A', 'Available')
    )

    seatNum = models.CharField(max_length=50, choices=SEATS, unique=True)
    status = models.CharField(max_length=50, choices=STATUS) 

class Booking(models.Model):
    movie = models.CharField(choices=[(movie.title, movie.title) for movie in Movie.objects.all()], max_length=100)
    date = models.DateField(default=timezone.now())
    seat = models.CharField(choices=[(seat.seatNum, seat.seatNum) for seat in Seat.objects.all() if seat.status != 'R'], max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    seat.status = 'R'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'seat'], name='one_seat_per_person')
        ]