from rest_framework import serializers
from products.models import Services, ContactLink




class ContactLinkSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = ContactLink
        fields = ['id', 'contact_type', 'value']

class ServicesSerializerConfig(serializers.ModelSerializer):
    contacts = ContactLinkSerializerConfig(many=True, read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'name', 'description', 'image', 'price', 'contacts']
