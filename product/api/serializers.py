from rest_framework import serializers
from product.models import *


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['slug', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['slug', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['slug', 'name']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    category = CategorySerializer(many=False)
    currency = CurrencySerializer(many=False)
    tag = TagSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','category', 'brand', 'slug', 'name',
                  'description', 'price', 'currency', 'is_active', 'tag']

class CreateUpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'brand', 'name', 'description', 'price', 'currency', 'tag','is_active']