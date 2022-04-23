
from django.db import models
from environment.models import Environment
from threats.models import Threats
from django.contrib.auth.models import User
# Create your models here.


class Whale(models.Model):  # inside the brackets is where its inheriting from
    """Whale is a child class of the Django `Model` class"""

    name = models.CharField(max_length=50)
    species_status = models.CharField(max_length=50)
    lifespan = models.CharField(max_length=20)
    image = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    environment = models.ForeignKey(
        Environment, related_name="whales", on_delete=models.CASCADE, null=True, blank=True)
    supporting_environment = models.ManyToManyField(Environment, blank=True)
    creator = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="whales")
    threat = models.ManyToManyField(
        Threats, blank=True, related_name="whales")

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.name} - {self.species_status}"
