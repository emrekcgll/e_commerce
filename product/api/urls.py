from django.urls import path
from product.api.views import *

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    path('category/<slug:slug>/', ProductListByCategory.as_view()),
    path('brand-list/', BrandListView.as_view()),
    path('brand/<slug:slug>/', ProductListByBrand.as_view()),
    path('product-list/', ProductListView.as_view()),
    path('product/<slug:slug>/', ProductDetailsView.as_view()),
]
