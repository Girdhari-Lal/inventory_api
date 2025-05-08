from django.db import models
from inventory.models import Attribute
# Model representing values of a given attribute (e.g., Red for Color)
class AttributeValue(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"