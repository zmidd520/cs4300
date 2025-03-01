from django.urls import include, path
from . import views

urlpatterns = [
    # index/movie list
    path('', views.movie_list, name='movie_list'),

    # debug urls to add non-user-created models
    path('movies/add', views.add_movie, name='add_movie'),

    # booking
    path('movies/<int:movie_id>/book', views.book_seat, name='book_seat'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page')
]