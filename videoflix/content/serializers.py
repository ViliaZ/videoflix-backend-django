
from .models import Movie
from rest_framework import serializers


class MovieDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'file']