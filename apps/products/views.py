from rest_framework import viewsets
from django.shortcuts import render

from .models import *
from .serializers import *


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related(
        'main'
    )
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related(
        'brand',
        'category'
    ).prefetch_related(
        'variations'
    )
    serializer_class = ProductSerializer


class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
