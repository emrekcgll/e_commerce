from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Cart, CartItem

@receiver(user_logged_in)
def merge_cart(sender, user, request, **kwargs):
    session_key = request.session.session_key
    if session_key:
        try:
            session_cart = Cart.objects.get(session_key=session_key)
            user_cart, created = Cart.objects.get_or_create(user=user)

            for item in session_cart.items.all():
                user_cart_item, item_created = CartItem.objects.get_or_create(cart=user_cart, product=item.product)
                user_cart_item.quantity += item.quantity
                user_cart_item.save()

            session_cart.delete()
        except Cart.DoesNotExist:
            pass