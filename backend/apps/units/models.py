from django.db import models
from apps.properties.models import Property

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="units")
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=2)

    def __str__(self):
        return f"{self.property.name} – {self.name}"