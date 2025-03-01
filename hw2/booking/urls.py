from django.urls import include, path
from . import views

urlpatterns = [
    # index/movie list
    path('', views.movie_list, name='movie_list'),

    # debug urls to add non-user-created models
    path('movies/add', views.add_movie, name='add_movie'),

    # booking
    path('book/<int:movie_id>', views.book_seat, name='book_seat'),
    path('<int:user_id>/bookings', views.booking_list, name='booking_list'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page')
]