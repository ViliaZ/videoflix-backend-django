from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import MovieDetailsSerializer
from .models import Movie
from users.admin import is_authenticated

class MovieDetails (viewsets.ModelViewSet):
  
    queryset = Movie.objects.all()
    serializer_class = MovieDetailsSerializer
    #permission_classes = []  # permissions.IsAdminUser
    #authentication_classes = [] # authentication.TokenAuthentication
    #return Response({'message': 'movies Endpoint'})