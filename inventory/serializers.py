from rest_framework import serializers
from inventory.models import Unit, Brand, Attribute, AttributeValue, Product, ProductAttribute

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = AttributeValue
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    # unit_of_measure = UnitSerializer()

    class Meta:
        model = Product
        fields = '__all__'

class ProductAttributeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    attribute_value = AttributeValueSerializer()

    class Meta:
        model = ProductAttribute
        fields = '__all__'