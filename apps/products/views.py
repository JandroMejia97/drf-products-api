from rest_framework import viewsets
from django.shortcuts import render

from .models import *
from .serializers import *


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    search_fields = ('name',)
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related(
        'main'
    )
    search_fields = ('name',)
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related(
        'brand',
        'category'
    ).prefetch_related(
        'variations'
    )
    filterset_fields = ('brand', 'category',)
    search_fields = ('name', 'category__name', 'brand__name',)
    serializer_class = ProductSerializer


class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    filterset_fields = ('product',)
    search_fields = ('product__name',)
    serializer_class = VariationSerializer
