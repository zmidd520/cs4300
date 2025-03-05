from django.urls import include, path
from . import views
from rest_framework import routers

# Router setup
router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movies')
router.register(r'seats', views.SeatViewSet, basename='seats')
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    # api
    path('api/', include(router.urls)),

    # index/movie list
    path('', views.movie_list, name='movie_list'),

    # booking
    path('book/<int:movie_id>', views.book_seat, name='book_seat'),
    path('user/<int:user_id>/bookings', views.booking_list, name='booking_list'),

    # account management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page'),

    # update seat information in database so the API returns the intended info
    path('seats/', views.setSeats, name='setSeats')
]