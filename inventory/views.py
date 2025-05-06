from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductAttribute, Brand, Unit
from inventory.serializers import ProductSerializer, ProductAttributeSerializer, BrandSerializer, UnitSerializer
from rest_framework import status

class BrandListAndCreateView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnitListCreateView(APIView):
    def get(self, request):
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductCreateAndListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

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

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProductAttributeCreateAndListView(APIView):
    def get(self, request):
        product_attributes = ProductAttribute.objects.all()
        serializer = ProductAttributeSerializer(product_attributes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAttributeView(APIView):
    def get(self, request, pk):
        try:
            product_attribute = ProductAttribute.objects.get(pk=pk)
        except ProductAttribute.DoesNotExist:
            return Response({"error": "ProductAttribute not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductAttributeSerializer(product_attribute)
        return Response(serializer.data)

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

    def delete(self, request, pk):
        try:
            product_attribute = ProductAttribute.objects.get(pk=pk)
        except ProductAttribute.DoesNotExist:
            return Response({"error": "ProductAttribute not found"}, status=status.HTTP_404_NOT_FOUND)
        product_attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)