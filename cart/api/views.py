from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import Cart, CartItem
from product.models import Product
from cart.api.serializers import CartSerializer, CartItemSerializer
from product.api.serializers import ProductSerializer


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    print(cart, created)
    return cart


@api_view(['GET'])
def cart_detail(request):
    cart = get_cart(request)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    cart = get_cart(request)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 0})
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    return Response({"success": "Item added to cart"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def update_cart_item(request):
    cart_item_id = request.data.get('cart_item_id')
    quantity = request.data.get('quantity')

    try:
        cart_item = CartItem.objects.get(id=cart_item_id, cart=get_cart(request))
    except CartItem.DoesNotExist:
        return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

    if quantity <= 0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()

    return Response({"success": "Cart item updated"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def remove_from_cart(request):
    cart_item_id = request.data.get('cart_item_id')

    try:
        cart_item = CartItem.objects.get(id=cart_item_id, cart=get_cart(request))
    except CartItem.DoesNotExist:
        return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

    cart_item.delete()

    return Response({"success": "Item removed from cart"}, status=status.HTTP_200_OK)