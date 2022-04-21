from django.db import models
from django.forms import CharField

# Create your models here.


class Environment(models.Model):
    region = models.CharField(max_length=50)
    # threats = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.region}'
