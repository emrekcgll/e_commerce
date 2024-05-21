from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from product.models import *
from product.api.serializers import *
from product.api.paginations import *


class ProductCreateView(CreateAPIView):
    serializer_class = CreateUpdateProductSerializer
    queryset = Product
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class ProductUpdateView(RetrieveUpdateAPIView):
    serializer_class = CreateUpdateProductSerializer
    queryset = Product
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class ProductDeleteView(DestroyAPIView):
    serializer_class = CreateUpdateProductSerializer
    queryset = Product
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class CategoryUpdateView(RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class CategoryDeleteView(DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]


class BrandCreateView(CreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class BrandUpdateView(RetrieveUpdateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class BrandDeleteView(DestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]


class TagCreateView(CreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class TagUpdateView(RetrieveUpdateAPIView):
    serializer_class = TagSerializer
    queryset = Tag
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class TagDeleteView(DestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag
    permission_classes = [IsAdminUser]


class CurrencyCreateView(CreateAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class CurrencyUpdateView(RetrieveUpdateAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class CurrencyDestroyView(DestroyAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]
