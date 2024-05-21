from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from product.models import *
from product.api.serializers import *
from product.api.paginations import *


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True).order_by('slug')


class ProductListByCategory(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        category = Category.objects.filter(slug=category_slug).first()
        return Product.objects.filter(category__is_active=True, brand__is_active=True,
                                      is_active=True, category=category).select_related('category', 'brand').order_by('slug')


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.filter(is_active=True)


class ProductListByBrand(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    lookup_field = 'slug'

    def get_queryset(self):
        brand_slug = self.kwargs.get('slug')
        brand = Brand.objects.filter(slug=brand_slug).first()
        return Product.objects.filter(category__is_active=True, brand__is_active=True,
                                      is_active=True, brand=brand).select_related('category', 'brand').order_by('slug')


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Product.objects.filter(category__is_active=True, brand__is_active=True,
                                      is_active=True).select_related('category', 'brand').order_by('slug')


class ProductDetailsView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Product.objects.filter(category__is_active=True, brand__is_active=True,
                                      is_active=True).select_related('category', 'brand').first()
