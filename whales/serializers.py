
from rest_framework import serializers
from whales.models import Whale


class WhalesSerializer(serializers.ModelSerializer):

    environment = serializers.SlugRelatedField(
        slug_field="region", read_only=True)

    supporting_environment = serializers.SlugRelatedField(
        slug_field="region", many=True, read_only=True)

    class Meta:
        model = Whale
        fields = '__all__'
