


from rest_framework import serializers

from environment.models import Environment
from threats.models import Threats
from whales.models import Whale


class ThreatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Threats
        fields = ("threat",)

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ("region",)


class WhalesSerializer(serializers.ModelSerializer):

    threat = serializers.SlugRelatedField(
        slug_field="threat", read_only=True, many=True)

    environment = serializers.SlugRelatedField(
        slug_field="region", read_only=True)

    supporting_environment = serializers.SlugRelatedField(
        slug_field="region", many=True, read_only=True)

    class Meta:
        model = Whale
        fields = '__all__'

    def create(self, data):
        threat_data = data.pop("threat")
        environment_data = data.pop("environment")
        whale = Whale(**data)

        if threat_data:
            threat, _created

#** is pass in the key and the data
        whale = Whale(**data)
        threat, _created = Threats.objects.get_or_create(**threat_data)
        whale.threat = threat
        whale.save()
        # data doesn't have creator_data
        return whale

    # def update(self, whale, data):
    #     threat_data = data.pop("threat")

    #     whale.name = data.get("name", whale.name)
    #     whale.species_status = data.get("species_status", whale.species_status)
    #     whale.lifespan = data.get("lifespan", whale.lifespan)
    #     whale.image = data.get(
    #         "image", whale.image)

    #     if threat_data:
    #         threat, _created = Threats.objects.get_or_create(**threat_data)
    #         whale.threat = threat

    #     whale.save()

    #     return whale
