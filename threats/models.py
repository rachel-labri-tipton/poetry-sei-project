from django.db import models

# Create your models here.


class Threats(models.Model):
    threat = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.threat}'
