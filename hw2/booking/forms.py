from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MovieForm(ModelForm):
    class Meta: 
        model = Movie 
        fields = ('title', 'description', 'releaseDate', 'duration')

class SeatForm(ModelForm):
    class Meta: 
        model = Seat
        fields = ('seatNum', 'status')

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('movie', 'date', 'seat')
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']