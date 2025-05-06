from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)  

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    PRODUCT_TYPE_CHOICES = [
        ('consu', 'Goods'),
        ('service', 'Service'),
        ('combo', 'Combo'),
    ]
    type = models.CharField(
        max_length=10,
        choices=PRODUCT_TYPE_CHOICES,
        default='consu',
    )
    can_be_sold = models.BooleanField(
        default=True,
    )
    available_in_pos = models.BooleanField(
        default=False,
    )
    description = models.TextField(blank=True)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0
    )
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0
    )
    category = models.CharField(max_length=50, null=True) 
    unit_of_measure = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.SET_NULL)
    weight_in_kg = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, null=True)
    volume_in_liters = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name
    
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('product', 'attribute_value')