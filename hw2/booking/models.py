from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    releaseDate = models.DateField(default=None)
    duration = models.TimeField()

    def __str__(self):
        return self.title

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

    seatNum = models.CharField(max_length=50, choices=SEATS)
    status = models.CharField(max_length=50, choices=STATUS, default='A') 

    # tie each seat to a specific movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.seatNum

class Booking(models.Model):
    movie = models.CharField(choices=[(movie.title, movie.title) for movie in Movie.objects.all()], max_length=100)
    date = models.DateField(default=timezone.now().date())
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            # prevent duplicate seat bookings
            models.UniqueConstraint(fields=['movie', 'seat', 'date'], name='one_seat_per_person_per_day')
        ]