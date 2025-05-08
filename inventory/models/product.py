from django.db import models
from django.core.validators import MinValueValidator
from inventory.models import TimeStampedModel
from inventory.models import Brand
from inventory.models import Category
from inventory.models import Unit
from users.models import User

# Model representing main product information
class Product(TimeStampedModel):
    id = models.AutoField(primary_key=True)
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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    @property
    def variant_count(self):
        return self.productattribute_set.count()