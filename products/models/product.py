from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.TextField()

    image = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video = models.URLField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,  # Masalan: 10.0 (jami 3 ta raqam)
        decimal_places=1,  # Verguldan keyin 1 ta raqam
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ],
        null=True, blank=True,
        help_text="1 dan 10 gacha ball bering"
    )

    qoldiq = models.IntegerField(default=0)
    size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    service = models.ForeignKey('Services', on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def clean(self):
        filled = [self.product, self.comment, self.service]
        filled_count = sum(1 for x in filled if x is not None)

        if filled_count == 0:
            raise ValidationError("product, comment yoki service bo'lishi shart!")

        if filled_count > 1:
            raise ValidationError("Faqat bittasi bo'lishi kerak!")








