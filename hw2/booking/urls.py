from django.urls import include, path
from . import views
from rest_framework import routers

# Router setup
router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'bookseats', views.BookSeatViewSet)

urlpatterns = [
    # api
    path('api/', include(router.urls)),

    # index/movie list
    path('', views.movie_list, name='movie_list'),

    # booking
    path('book/<int:movie_id>', views.book_seat, name='book_seat'),
    path('user/<int:user_id>/bookings', views.booking_list, name='booking_list'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page')
]