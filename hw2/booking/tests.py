from django.test import TestCase
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import *
import datetime

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

# test CRUD operations for movie objects
class TestMovieView(APITestCase):
    # set up test objects
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@test.test')
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(title='Test Movie', description='testing', releaseDate='2025-03-03', duration='02:00:00')

    # test that the list of movies is returned correctly
    def test_get_movies(self):
        url = reverse('movies-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = MovieSerializer([self.movie], many=True).data
        self.assertEqual(response.data, serializer_data)

    # test that a movie can be added via the api
    def test_add_movie(self):
        url = reverse('movies-list')
        movie_info = {
            'title': 'New Movie',
            'description': 'movie added via API',
            'releaseDate': '2025-03-04',
            'duration': '01:30'
        }
        response = self.client.post(url, movie_info)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(title='New Movie')
        
        self.assertEqual(movie_info['title'], movie.title)
        self.assertEqual(movie_info['description'], movie.description)
        self.assertEqual(movie_info['releaseDate'], movie.releaseDate.strftime('%Y-%m-%d'))
        self.assertEqual(datetime.datetime.strptime(movie_info['duration'], '%H:%M').time(), movie.duration)

    # test that a movie can be retrieved via the api
    def test_retrieve_movie(self):
        url = reverse('movies-detail', args=[self.movie.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = MovieSerializer(self.movie).data
        self.assertEqual(response.data, serializer_data)

    # test that a movie can be updated via the api
    def test_update_movie(self):
        url = reverse('movies-detail', args=[self.movie.pk])
        movie_info = {
            'title': 'Updated Movie',
            'description': 'movie updated via API',
            'releaseDate': '2025-03-05',
            'duration': '02:00'
        }
        response = self.client.put(url, movie_info)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movie = Movie.objects.get(pk=self.movie.pk)
        self.assertEqual(movie.title, movie_info['title'])

    # test that a movie can be deleted via the api
    def test_delete_movie(self):
        url = reverse('movies-detail', args=[self.movie.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())

# test that the API returns a list of seats in the theater
class TestSeatView(APITestCase):
    # set up test objects
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@test.test')
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(title='Test Movie', description='testing', releaseDate='2025-03-03', duration='02:00:00')
        self.seat1 = Seat.objects.create(seatNum='A1', status='A', movie=self.movie)
        self.seat2 = Seat.objects.create(seatNum='A2', status='R', movie=self.movie)

    # test that the list of seats is returned correctly
    def test_get_seats(self):
        url = reverse('seats-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = SeatSerializer([self.seat1, self.seat2], many=True).data
        self.assertEqual(response.data, serializer_data)

# test that bookings can be made and history can be viewed via the API
class TestBookingView(APITestCase):
    # set up test objects
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@test.test')
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(title='Test Movie', description='testing', releaseDate='2025-03-03', duration='02:00')
        self.seat1 = Seat.objects.create(seatNum='A1', status='A', movie=self.movie)
        self.seat2 = Seat.objects.create(seatNum='A2', status='A', movie=self.movie)
        self.seat3 = Seat.objects.create(seatNum='C3', status='A', movie=self.movie)
        self.booking1 = Booking.objects.create(movie='Test Movie', date='2025-03-03', seat=self.seat1, user=self.user)
        self.booking2 = Booking.objects.create(movie='Test Movie', date='2025-03-03', seat=self.seat2, user=self.user)

    # test that the list of bookings is returned correctly
    def test_get_bookings(self):
        url = reverse('bookings-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = BookingSerializer([self.booking1, self.booking2], many=True).data
        self.assertEqual(response.data, serializer_data)

    # test that a booking can be made via the api
    def test_create_booking(self):
        url = reverse('bookings-list')
        booking_info = {
            'movie': 'Dog Man',     # test only works with movies in "prod" database
            'date': '2025-03-03',
            'seat': self.seat3.pk,
            'user': self.user
        }
        response = self.client.post(url, booking_info)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test that the api catches duplicate seat/date selections
    def test_dupe_booking(self):
        url = reverse('bookings-list')
        booking_info = {
            'movie': 'Dog Man',     # test only works with movies in "prod" database
            'date': '2025-03-03',
            'seat': self.seat3.pk,
            'user': self.user
        }
        response = self.client.post(url, booking_info)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(url, booking_info)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) # my custom error response uses 400 as the response code
        