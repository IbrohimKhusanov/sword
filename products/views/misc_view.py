from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from django_filters import rest_framework as django_filters
from rest_framework import filters

from products.filters.misc_filter import CommentsFilter, OrderFilter, OrderItemsFilter

from products.models import Comments, Order, OrderItems
from products.serializers import CommentsSerializerConfig, OrderSerializerConfig, OrderItemsSerializerConfig

class CustomPagination(PageNumberPagination):
    page_size = 5



class CommentsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = CommentsFilter
    search_fields = ['comment', 'rating']
    pagination_class = CustomPagination


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    serializer_class = OrderSerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = OrderFilter
    search_fields = ['status', 'phone_number', 'user__phone_number', 'user__first_name']
    pagination_class = CustomPagination


class OrderItemsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = OrderItemsFilter
    search_fields = ['address', 'product__name', 'phone_number', 'product__description']
    pagination_class = CustomPagination
