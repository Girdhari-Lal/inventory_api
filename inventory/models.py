from django.db import models
from django.core.validators import MinValueValidator

class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)  

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
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
    
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(
        max_length=10,
        choices=[('consu', 'Goods'), ('service', 'Service'), ('combo', 'Combo')],
        default='consu',
    )
    can_be_sold = models.BooleanField(
        default=True,
    )
    available_in_pos = models.BooleanField(
        default=False,
    )
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) 
    unit_of_measure = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    weight_in_kg = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, null=True, blank=True, validators=[MinValueValidator(0)])
    volume_in_liters = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
    @property
    def variant_count(self):
        return self.productattribute_set.count()

    
class ProductAttribute(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0., validators=[MinValueValidator(0)])
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