

from rest_framework import serializers

from threats.models import Threats


class ThreatsSerializer(serializers.ModelSerializer):

    # link = serializers.SerializerMethodField("get_link_from_id")

    class Meta:
        model = Threats
        fields = ("threat", "whales")

    # def get_link_from_id(self, threat):
    #     return f"http://localhost:8000/creators/{threat.id}"
