from rest_framework import serializers

from .models import *


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = ('__all__')


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    brand = BrandSerializer(many=False)

    class Meta:
        model = Product
        exclude = ('likes_count', 'discount', 'is_new', 'url',)


class ProductSerializer(ProductListSerializer):
    variations = VariationSerializer(many=True)

    class Meta:
        model = Product
        fields = ('__all__')
