from django.shortcuts import render
from .models import *
from django.views import generic
from rest_framework import viewsets
from rest_framework.response import Response
from booking.serializers import MovieSerializer

# Web Views
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'booking/index.html', context)

# ViewSets
class MovieViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Movies.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)