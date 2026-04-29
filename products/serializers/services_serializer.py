from rest_framework import serializers
from products.models import Services

class ServicesSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"