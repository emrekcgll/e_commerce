from django.urls import path
from cart.api.views import *

urlpatterns = [
    path('', cart_detail),
    path('add/', add_to_cart),
    path('update/', update_cart_item),
    path('remove/', remove_from_cart),
]
