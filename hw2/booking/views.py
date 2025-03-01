from django.shortcuts import render, redirect
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

    if request.method == "POST":
        booking_data = request.POST.copy()

        form = BookingForm(booking_data)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.movie = movie.title
            booking.save()
            messages.success(request, "Seat booked!")
        return(redirect('booking_list', request.user.id))
    
    context = {'movie': movie, 'form': form}
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

'''
# ViewSets
class MovieViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Movies.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        
    
    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(user)
        return Response(serializer.data)
'''