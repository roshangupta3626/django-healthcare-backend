from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []  # allow anyone to register

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
