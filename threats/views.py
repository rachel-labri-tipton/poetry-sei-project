from django.shortcuts import render
from backend import permissions
from rest_framework import generics
# Create your views here.

from .models import Threats

from .serializers import ThreatsSerializer


class ThreatsView(generics.ListCreateAPIView):
    queryset = Threats.objects.all()
    serializer_class = ThreatsSerializer


class ThreatDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsReadOnly,)
    queryset = Threats.objects.all()
    serializer_class = ThreatsSerializer
