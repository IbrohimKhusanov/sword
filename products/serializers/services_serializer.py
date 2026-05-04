from rest_framework import serializers
from products.models import Services, ContactLink




class ContactLinkSerializerConfig(serializers.ModelSerializer):
    class Meta:
        model = ContactLink
        fields = ['id', 'contact_type', 'value']

class ServicesSerializerConfig(serializers.ModelSerializer):
    contacts = ContactLinkSerializerConfig(many=True, read_only=False)

    class Meta:
        model = Services
        fields = ['id', 'name', 'description', 'image', 'price', 'contacts']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        service = Services.objects.create(**validated_data)
        for contact in contacts_data:
            ContactLink.objects.create(service=service, **contact)
        return service
