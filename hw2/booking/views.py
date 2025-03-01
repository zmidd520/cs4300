from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import generic
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from booking.serializers import MovieSerializer

# Web Views
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'booking/movie_list.html', context)

@login_required
def book_seat(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    form = BookingForm()

    if request.method == "POST":
        booking_data = request.POST.copy()

        form = BookingForm(booking_data)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
        return(redirect('movie_list'))
    
    context = {'movie': movie, 'form': form}
    return render(request, 'booking/booking_form.html', context)

def add_movie(request):
    form = MovieForm()

    if request.method == "POST":
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

def registerPage(request):
      form = CreateUserForm()

      if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  username = form.cleaned_data.get('username')
                  group = Group.objects.get(name='user')
                  user.groups.add(group)
                  account = Account.objects.create(user=user,)
                  account.save()

                  messages.success(request, 'Account was created for ' + username)
                  return redirect('login')
       
      context = {'form': form}
      return render(request, 'registration/register.html', context)

# ViewSets
class MovieViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Movies.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)