from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),

    # debug urls to add non-user-created models
    path('movies/add', views.add_movie, name='add_movie'),
    path('seats/add', views.add_seat, name='add_seat'),

    path('movies/<int:movie_id>/seats', views.movie_seats, name='movie_seats')
]