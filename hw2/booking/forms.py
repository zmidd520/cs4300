from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MovieForm(forms.ModelForm):
    class Meta: 
        model = Movie 
        fields = ('title', 'description', 'releaseDate', 'duration')

class SeatForm(forms.ModelForm):
    class Meta: 
        model = Seat
        fields = ('seatNum', 'status')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'seat')

        error_messages = {
            'seat': {
                'unique_for_date': "This seat is reserved, please choose a different seat",
                'one_seat_per_person': "This seat is reserved, please choose a different seat"},
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']