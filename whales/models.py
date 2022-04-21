
from django.db import models
from environment.models import Environment

# Create your models here.


class Whale(models.Model):  # inside the brackets is where its inheriting from
    """Whale is a child class of the Django `Model` class"""

    name = models.CharField(max_length=50)
    species_status = models.CharField(max_length=50)
    lifespan = models.CharField(max_length=20)
    image = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    environment = models.ForeignKey(
        Environment, related_name="name", on_delete=models.SET_NULL, null=True, )
    supporting_environment = models.ManyToManyField(
        Environment, blank=True)

    def __str__(self):
        """ represents the class objects as a string """
        return f"{self.name} - {self.species_status}"
