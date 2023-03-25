from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .serializers import ProductSerializer
from .models import Product
from datetime import datetime

class ProductDetails(APIView):
    """
    Retrieve, update or delete a product instance
    """
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
    """
    ProductList
    """
    def get(self, request): 
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)
