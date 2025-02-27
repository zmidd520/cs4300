from rest_framework import serializers
import booking.models

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    decription = serializers.CharField(required=True, allow_blank=False, max_length=200)
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

