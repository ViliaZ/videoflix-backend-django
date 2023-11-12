from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import MovieDetailsSerializer
from .models import Movie
from users.admin import is_authenticated

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
class MovieDetails (viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailsSerializer
    permission_classes = []  # permissions.IsAdminUser
    authentication_classes = [] # authentication.TokenAuthentication

    method_decorator(cache_page(CACHE_TTL))
    def list(self, request):
            queryset = Movie.objects.all()
            serializer = MovieDetailsSerializer(queryset, many=True)
            return Response(serializer.data)
    
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, pk=None):
            movie = get_object_or_404(self.queryset, pk=pk)
            serializer = MovieDetailsSerializer(movie)
            return Response(serializer.data)

