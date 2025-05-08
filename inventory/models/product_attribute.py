from django.db import models
from inventory.models import TimeStampedModel
from inventory.models import Product
from inventory.models import Attribute
from inventory.models import AttributeValue
from django.core.validators import MinValueValidator

# Model representing a product variant with specific attribute value    
class ProductAttribute(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, validators=[MinValueValidator(0)]
    )
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, validators=[MinValueValidator(0)]
    )

    class Meta:
        unique_together = ('product', 'attribute_value')

    def __str__(self):
        return f"{self.product.name} - {self.attribute_value}"