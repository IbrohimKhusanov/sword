from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .product import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Comments(models.Model):
    commet = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,  # Masalan: 10.0 (jami 3 ta raqam)
        decimal_places=1,  # Verguldan keyin 1 ta raqam
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ],
        help_text="1 dan 10 gacha ball bering")
    image = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.user} on {self.product}"




ORDER_STATUS_CHOICES = [
    ('new', 'New'),
    ('sent', 'Sending'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='new', choices=ORDER_STATUS_CHOICES)  # pending, paid, shipped

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - Total: {self.total_price}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)  # Juda muhim!

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"

















