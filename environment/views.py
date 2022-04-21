from django.shortcuts import render
from rest_framework import generics
from environment.models import Environment
from environment.serializers import EnvironmentSerializer

# Create your views here. And there is the controller-like logic in the views


class EnvironmentListView(generics.ListCreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class EnvironmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
