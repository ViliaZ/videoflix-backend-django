from urllib import request
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer
from django.core import serializers
from rest_framework import status

class RegisterViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [] #permissions.isAuthenticated

