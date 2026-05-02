from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from django_filters import rest_framework as django_filters

from products.models import Services, ContactLink
from products.serializers import ServicesSerializerConfig, ContactLinkSerializerConfig
from products.filters import ServicesFilter, ContactLinkFilter
from rest_framework import filters



class CustomPagination(PageNumberPagination):
    page_size = 5



class ServicesViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ServicesFilter
    search_fields = ['name', 'description', 'price']
    pagination_class = CustomPagination


class ContactLinkViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ContactLinkFilter
    search_fields = ['value', 'contact_type']
    pagination_class = CustomPagination