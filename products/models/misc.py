from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()




ORDER_STATUS_CHOICES = [
    ('new', 'New'),
    ('sent', 'Sending'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be entered in the format: '+998xxxxxxxxx'. Up to 9 digits allowed."
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='new', choices=ORDER_STATUS_CHOICES)  # pending, paid, shipped

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - Total: {self.total_price}"




class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)  # Juda muhim!

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"

















