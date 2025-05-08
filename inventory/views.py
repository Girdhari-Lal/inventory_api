from rest_framework.response import Response
from rest_framework.views import APIView
from inventory.models import Product, ProductAttribute, Brand, Unit, Attribute, AttributeValue, Category
from inventory.serializers import ( ProductSerializer, ProductAttributeSerializer, BrandSerializer, 
            UnitSerializer, AttributeSerializer, AttributeValueSerializer, CategorySerializer)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 

# This api help to get List of all brands or create a new brand 
# http://127.0.0.1:8000/products/
class BrandListAndCreateView(APIView):
    permission_classes = [IsAuthenticated]
    # Return all brands
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    # Create a new brand
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# This api view help to Retrieve, update, or delete a single brand
# http://127.0.0.1:8000/products/id/
class BrandView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single brand by ID
    def get(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Update a brand
    def put(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)
    # Delete a brand    
    def delete(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)
        
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Unit API: List all units or create a new 
# http://127.0.0.1:8000/units/
class UnitListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    # Return all units
    def get(self, request):
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)
    # Create a new unit
    def post(self, request):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Unit API: Retrieve, update, or delete a single unit    
# http://127.0.0.1:8000/units/id/
class UnitView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single unit by ID
    def get(self, request, pk):
        try:
            unit = Unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            return Response({"error": "Unit not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UnitSerializer(unit)
        return Response(serializer.data)
    # Update a unit
    def put(self, request, pk):
        try:
            unit = Unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            return Response({"error": "Unit not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnitSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a unit
    def delete(self, request, pk):
        try:
            unit = unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            return Response({"error": "Unit not found"}, status=status.HTTP_404_NOT_FOUND)
        unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# Category API: List all categories or create a new one
# http://127.0.0.1:8000/categories/   
class CategoryListAndCreateView(APIView):
    permission_classes = [IsAuthenticated]
    # Return all categories
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    # Create a new category
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Category API: Retrieve, update, or delete a category
# http://127.0.0.1:8000/categories/id/   
class CategoryView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single category
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    # Update a category
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a category
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Product API: List all products or create a new one
# http://127.0.0.1:8000/products/   
class ProductCreateAndListView(APIView):
    permission_classes = [IsAuthenticated]
    # Return all products
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    # Create a new product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Product API: Retrieve, update, or delete a products
# http://127.0.0.1:8000/products/id/       
class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single products
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    # Update a products
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a products
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Attribute API: List all Attribute or create a new one
# http://127.0.0.1:8000/attributes/
class AttributeListAndCreateView(APIView):
    permission_classes = [IsAuthenticated]
    # Return all Attributes
    def get(self, request):
        attributes = Attribute.objects.all()
        serializer = AttributeSerializer(attributes, many=True)
        return Response(serializer.data)
    # Create a new Attribute
    def post(self, request):
        serializer = AttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Attribute API: Retrieve, update, or delete a Attribute
# http://127.0.0.1:8000/attributes/id         
class AttributeView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single Attribute
    def get(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
        except Attribute.DoesNotExist:
            return Response({"error": "Attribute not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttributeSerializer(attribute)
        return Response(serializer.data)
    # Update a Attribute
    def put(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
        except Attribute.DoesNotExist:
            return Response({"error": "Attribute not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttributeSerializer(attribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a Attribute
    def delete(self, request, pk):
        try:
            attribute = Attribute.objects.get(pk=pk)
        except Attribute.DoesNotExist:
            return Response({"error": "Attribute not found"}, status=status.HTTP_404_NOT_FOUND)
        attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

# Attribute-values API: List all Attribute value or create a new one
# http://127.0.0.1:8000/attribute-values/    
class AttributeValueListAndCreateView(APIView):
    permission_classes = [IsAuthenticated]
    # Return all Attributes value
    def get(self, request):
        attribute_values = AttributeValue.objects.all()
        serializer = AttributeValueSerializer(attribute_values, many=True)
        return Response(serializer.data)
    # Create a new Attribute value
    def post(self, request):
        serializer = AttributeValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Attribute Value API: Retrieve, update, or delete a Attribute
# http://127.0.0.1:8000/attribute-values/id      
class AttributeValueView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single Attribute
    def get(self, request, pk):
        try:
            attribute_value = AttributeValue.objects.get(pk=pk)
        except AttributeValue.DoesNotExist:
            return Response({"error": "Attribute Value not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttributeValueSerializer(attribute_value)
        return Response(serializer.data)
    # Update a Attribute
    def put(self, request, pk):
        try:
            attribute_value = AttributeValue.objects.get(pk=pk)
        except AttributeValue.DoesNotExist:
            return Response({"error": "Attribute Value not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AttributeValueSerializer(attribute_value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a Attribute
    def delete(self, request, pk):
        try:
            attribute_value = AttributeValue.objects.get(pk=pk)
        except AttributeValue.DoesNotExist:
            return Response({"error": "Attribute Value not found"}, status=status.HTTP_404_NOT_FOUND)
        attribute_value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Product Attribute API: List all Product Attribute value or create a new one
# http://127.0.0.1:8000/product-attributes/ 
class ProductAttributeCreateAndListView(APIView):
    permission_classes = [IsAuthenticated]
     # Return all Product Attributes value
    def get(self, request):
        product_attributes = ProductAttribute.objects.all()
        serializer = ProductAttributeSerializer(product_attributes, many=True)
        return Response(serializer.data)
    # Create a new Product Attribute value
    def post(self, request):
        serializer = ProductAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Product Attribute API: Retrieve, update, or delete a Product Attribute
# http://127.0.0.1:8000/product-attributes/id/ 
class ProductAttributeView(APIView):
    permission_classes = [IsAuthenticated]
    # Get a single Product Attribute
    def get(self, request, pk):
        try:
            product_attribute = ProductAttribute.objects.get(pk=pk)
        except ProductAttribute.DoesNotExist:
            return Response({"error": "ProductAttribute not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductAttributeSerializer(product_attribute)
        return Response(serializer.data)
    # Update a Product Attribute
    def put(self, request, pk):
        try:
            product_attribute = ProductAttribute.objects.get(pk=pk)
        except ProductAttribute.DoesNotExist:
            return Response({"error": "ProductAttribute not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductAttributeSerializer(product_attribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a Product Attribute 
    def delete(self, request, pk):
        try:
            product_attribute = ProductAttribute.objects.get(pk=pk)
        except ProductAttribute.DoesNotExist:
            return Response({"error": "ProductAttribute not found"}, status=status.HTTP_404_NOT_FOUND)
        product_attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)