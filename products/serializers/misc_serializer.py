from rest_framework import serializers
from products.models import Comments, Order, OrderItems


class CommentsSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"






class OrderItemsSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity', 'price_at_purchase']


class OrderSerializerConfig(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    items = OrderItemsSerializerConfig(many=True)
    class Meta:
        model = Order
        fields = ['phone_number', 'total_price', 'items', 'address']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItems.objects.create(order=order, **item_data)

        return order
