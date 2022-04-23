from rest_framework import serializers

from environment.models import Environment


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = ("region", "whales")
