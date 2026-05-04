from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import SendEmailResetSerializer

User = get_user_model()


class UserSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'first_name', 'address', 'is_active', 'is_staff', 'data_joined',
                  'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomPasswordResetSerializer(SendEmailResetSerializer):
    def get_user(self, is_active=True):
        email = self.data.get('email')
        try:
            return User.objects.get(email=email, is_active=is_active)
        except User.DoesNotExist:
            return None

