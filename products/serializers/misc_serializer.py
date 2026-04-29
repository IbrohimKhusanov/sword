from rest_framework import serializers
from products.models import Comments, Order, OrderItems


class CommentsSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"




class OrderSerializerConfig(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Order
        fields = "__all__"



class OrderItemsSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"