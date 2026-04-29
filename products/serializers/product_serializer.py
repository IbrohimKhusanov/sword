from rest_framework import serializers
from products.models import Product, Category


class ProductSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','qoldiq', 'size','image', 'price', 'category']


class CategorySerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']