from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'first_name', 'address', 'is_active', 'is_staff', 'data_joined']