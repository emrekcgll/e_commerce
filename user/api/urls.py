from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from user.api.views import *

urlpatterns = [
    # Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    # Admin permission required operations
    path('create-product/',ProductCreateView.as_view()),

    path('create-category/', CategoryCreateView.as_view()),
    path('update-category/<slug:slug>/', CategoryUpdateView.as_view()),
    path('delete-category/<slug:slug>/', CategoryDeleteView.as_view()),

    path('create-brand/', BrandCreateView.as_view()),
    path('update-brand/<slug:slug>/', BrandUpdateView.as_view()),
    path('delete-brand/<slug:slug>/', BrandDeleteView.as_view()),

    path('create-tag/', TagCreateView.as_view()),
    path('update-tag/<slug:slug>/', TagUpdateView.as_view()),
    path('delete-tag/<slug:slug>/', TagDeleteView.as_view()),

    path('create-currency/', CurrencyCreateView.as_view()),
    path('update-currency/<slug:slug>/', CurrencyUpdateView.as_view()),
    path('delete-currency/<slug:slug>/', CurrencyDestroyView.as_view()),
]
