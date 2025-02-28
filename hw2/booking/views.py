from django.shortcuts import render
from .models import *
from .forms import *
from django.views import generic
from rest_framework import viewsets
from rest_framework.response import Response
from booking.serializers import MovieSerializer

# Web Views
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'booking/movie_list.html', context)

def movie_seats(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    seats = Seat.objects.all()
    context = {'movie': movie, 'seats': seats}
    return render(request, 'booking/seats.html', context)

def add_movie(request):
    form = MovieForm()

    if request.method == "POST":
        # make dictionary with user id and reminder data
        movie_data = request.POST.copy()

        # get form data
        form = MovieForm(movie_data)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()

       
    context = {'form': form}
    return render(request, 'booking/movie_form.html', context)

def add_seat(request):
    form = SeatForm()

    if request.method == "POST":
        # make dictionary with user id and reminder data
        seat_data = request.POST.copy()

        # get form data
        form = SeatForm(seat_data)

        if form.is_valid():
            seat = form.save(commit=False)
            seat.save()

       
    context = {'form': form}
    return render(request, 'booking/seat_form.html', context)

# ViewSets
class MovieViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Movies.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)