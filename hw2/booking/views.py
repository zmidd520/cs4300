from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class MovieViewSet(viewsets.ViewSet):
    
    def list(self, request):
        pass