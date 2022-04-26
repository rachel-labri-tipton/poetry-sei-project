from django.shortcuts import render
from rest_framework import generics
from environment.models import Environment
from environment.serializers import EnvironmentSerializer


class EnvironmentListView(generics.ListCreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class EnvironmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
