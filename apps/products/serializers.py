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

    class Meta:
        model = Product
        exclude = ('likes_count', 'discount', 'is_new', 'url',)

    def to_representation(self, instance):
        response = super(ProductListSerializer,
                         self).to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class ProductSerializer(ProductListSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

    def to_representation(self, instance):
        response = super(ProductSerializer, self).to_representation(instance)
        response['variations'] = VariationSerializer(
            instance.variations.all(), many=True, read_only=True).data
        return response
