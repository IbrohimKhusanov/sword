from rest_framework import serializers
from products.models import Product, Category, Images


class ProductSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description','qoldiq', 'size', 'price', 'category']


class CategorySerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ImagesSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'image', 'product', 'comment', 'service']

    def validate(self, data):
        filled_count = sum(1 for x in [
            data.get('product'),
            data.get('comment'),
            data.get('service')
        ] if x is not None)

        if filled_count == 0:
            raise serializers.ValidationError("product, comment yoki service bo'lishi shart!")

        if filled_count > 1:
            raise serializers.ValidationError("Faqat bittasi bo'lishi kerak!")

        return data