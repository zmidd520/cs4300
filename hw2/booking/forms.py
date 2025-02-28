from django.forms import ModelForm
from .models import *

class MovieForm(ModelForm):
    class Meta: 
        model = Movie 
        fields = ('title', 'description', 'releaseDate', 'duration')

class SeatForm(ModelForm):
    class Meta: 
        model = Seat
        fields = ('seatNum', 'status')