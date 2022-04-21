
from rest_framework import serializers
from whales.models import Whale


class WhalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whale
        fields = '__all__'
