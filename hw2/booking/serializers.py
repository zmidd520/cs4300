from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(required=True, allow_blank=False, max_length=200)
    releaseDate = serializers.DateField(required=True)
    duration = serializers.TimeField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.releaseDate = validated_data.get('releaseDate', instance.releaseDate)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance

class SeatSerializer(serializers.Serializer):
    movie = serializers.CharField(read_only=True)
    seatNum = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    # get lists of movie names and seat numbers
    movies = []
    for movie in Movie.objects.all():
        movies.append(movie.title)

    movie = serializers.ChoiceField(choices=movies)
    date = serializers.DateField(required=True)
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())

    def create(self, validated_data):
        # include current user when creating new booking
        return Booking.objects.create(user=self.context['request'].user, **validated_data)

    
        

