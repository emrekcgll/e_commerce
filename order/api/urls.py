from django.urls import path
from order.api.views import order_list, create_order

urlpatterns = [
    path("", order_list),
    path("create/", create_order),
]
