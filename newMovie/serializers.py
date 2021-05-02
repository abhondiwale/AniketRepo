from rest_framework import serializers
from .models import newMovieModel


class MoviesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    director = serializers.CharField(max_length=100)
    ratings = serializers.IntegerField()
    date = serializers.DateField()
