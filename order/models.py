from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,
                              choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
                              default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    @property
    def total_price(self):
        base_total = sum(item.total_price for item in self.items.all())
        shipping_fee = 25 if base_total < 200 else 0
        return base_total + shipping_fee
    
    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.price

    class Meta:
        db_table = 'order_item'
