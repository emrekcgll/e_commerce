from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from order.models import Order, OrderItem
from order.api.serializers import OrderSerializer
from cart.api.views import get_cart

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    orders = Order.objects.filter(user=request.user).select_related('user').prefetch_related('items__product')

    # Her sipariş için toplam fiyatı hesapla
    order_data = []
    for order in orders:
        order_data.append({
            'id': order.id,
            'user': order.user.username if order.user else 'Anonymous',
            'session_key': order.session_key,
            'created_at': order.created_at,
            'updated_at': order.updated_at,
            'status': order.status,
            'items': [{
                'product': item.product.name,
                'quantity': item.quantity,
                'price': item.price,
                'total_price': item.total_price,
            } for item in order.items.all()],
            'total_price': order.total_price,
        })

    return Response(order_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_order(request):
    cart = get_cart(request)
    if not cart.items.exists():
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

    order = Order.objects.create(user=request.user if request.user.is_authenticated else None)

    order_items = []
    for item in cart.items.select_related('product').all():
        order_items.append(OrderItem(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        ))

    OrderItem.objects.bulk_create(order_items)
    
    # Payment
        
    # Clear the cart
    cart.items.all().delete()
    cart.delete()

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)