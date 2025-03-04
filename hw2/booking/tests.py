from django.test import TestCase
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

# Create your tests here.
class ModelTests(TestCase):
    # set up test objects
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@test.test')
        self.movie = Movie.objects.create(title='Test Movie', description='testing', releaseDate='2025-03-03', duration='02:00')
        self.seat = Seat.objects.create(seatNum='A1', status='A', movie=self.movie)
        self.booking = Booking.objects.create(movie='Test Movie', date='2025-03-03', seat=self.seat, user=self.user)
    
    # check that movie info is correct
    def test_movie_info(self):
        self.assertEqual(self.movie.title, 'Test Movie')
        self.assertEqual(self.movie.description, 'testing')
        self.assertEqual(self.movie.releaseDate, '2025-03-03')
        self.assertEqual(self.movie.duration, '02:00')

    # check that seat info is correct
    def test_seat_info(self):
        self.assertEqual(self.seat.seatNum, 'A1')
        self.assertEqual(self.seat.status, 'A')
        self.assertEqual(self.seat.movie, self.movie)

    # check that booking info is correct
    def test_booking_info(self):
        self.assertEqual(self.booking.movie, 'Test Movie')
        self.assertEqual(self.booking.date, '2025-03-03')
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

