from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    image = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    qoldiq = models.IntegerField(default=0)
    size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name










