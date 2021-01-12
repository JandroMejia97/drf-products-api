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


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    category = CategorySerializer(many=False)
    variations = VariationSerializer(many=True)

    class Meta:
        model = Product
        fields = ('__all__')