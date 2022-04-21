from rest_framework import serializers

from environment.models import Environment


class EnvironmentSerializer():

    class Meta:
        model = Environment
        fields = ("region")
