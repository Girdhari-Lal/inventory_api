from rest_framework import serializers
from inventory.models import Unit, Brand, Attribute, AttributeValue, Product, ProductAttribute, Category

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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class AttributeValueSerializer(serializers.ModelSerializer):
    # attribute = AttributeSerializer()

    class Meta:
        model = AttributeValue
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    variant_count = serializers.SerializerMethodField()
    # brand = BrandSerializer()
    # unit_of_measure = UnitSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_by']

    def get_variant_count(self, obj):
        return obj.variant_count
class ProductAttributeSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    # attribute_value = AttributeValueSerializer(read_only=True)

    class Meta:
        model = ProductAttribute
        fields = '__all__'