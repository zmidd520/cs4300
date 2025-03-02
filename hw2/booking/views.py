from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import *
from .forms import *
from django.views import generic
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from booking.serializers import MovieSerializer

# Web Views
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'booking/movie_list.html', context)

@login_required
def booking_list(request, user_id):
    bookings = Booking.objects.all()

    context = {'bookings': bookings}
    return render(request, 'booking/booking_list.html', context)

@login_required
def book_seat(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    form = BookingForm()

    context = {'movie': movie, 'form': form}

    if request.method == "POST":
        booking_data = request.POST.copy()

        form = BookingForm(booking_data)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.movie = movie.title

            # attempt to book seat
            try:
                booking.save()
                messages.success(request, "Seat booked!")

            # error occurs if seat is booked
            except IntegrityError:
                messages.error(request, "That seat has been booked for this day, please choose a different seat or book for a later date")
                return render(request, 'booking/booking_form.html', context)
        else:        
            messages.error(request, "Something went wrong, try booking again")  
            return render(request, 'booking/booking_form.html', context)

        return(redirect('booking_list', request.user.id))
    
    return render(request, 'booking/booking_form.html', context)

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

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
