from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from .product import Product
from django.contrib.auth import get_user_model

User = get_user_model()



class Comments(models.Model):
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,  # Masalan: 10.0 (jami 3 ta raqam)
        decimal_places=1,  # Verguldan keyin 1 ta raqam
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ],
        help_text="1 dan 10 gacha ball bering")
    video = models.URLField(null=True, blank=True)


    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.user} on {self.product}"


