from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    releaseDate = models.DateField(default=None)
    duration = models.TimeField()

class Seat(models.Model):
    # choices for seat number
    SEATS = (
        (1, 'A1'),  (2, 'A2'),  (3, 'A3'),  (4, 'A4'),  (5, 'A5'),        
        (6, 'B1'),  (7, 'B2'),  (8, 'B3'), (9, 'B4'), (10, 'B5'),    
        (11, 'C1'), (12, 'C2'), (13, 'C3'), (14, 'C4'), (15, 'C5'),    
        (16, 'D1'), (17, 'D2'), (18, 'D3'), (19, 'D4'), (20, 'D5'),   
        (21, 'E1'), (22, 'E2'), (23, 'E3'), (24, 'E4'), (25, 'E5'), 
        (26, 'F1'), (27, 'F2'), (28, 'F3'), (29, 'F4'), (30, 'F5')    
    )

    # choices for seat status
    STATUS = (
        ('R', 'Reserved'),
        ('A', 'Available')
    )

    seatNum = models.CharField(max_length=50, choices=SEATS, unique=True)
    status = models.CharField(max_length=50, choices=STATUS)

    # make seat selection unique on a per-movie basis
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('movie_seats', args=[str(self.movie.id)])

    class Meta:
        unique_together = ('movie', 'seatNum')

class Booking(models.Model):
    date = models.DateField(default=None)
    movie = models.CharField(choices=[(movie.id, movie.title) for movie in Movie.objects.all()], max_length=100)
    seat = models.CharField(choices=[seat.seatNum for seat in Seat.objects.all()], max_length=10, unique_for_date=date, unique=True)  # only display available seats for the given date
    user = models.OneToOneField(User, on_delete=models.CASCADE)