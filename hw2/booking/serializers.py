from rest_framework import serializers
import booking.models

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    

