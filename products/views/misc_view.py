from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from django_filters import rest_framework as django_filters

from products.models import Comments, Order, OrderItems
from products.serializers import CommentsSerializerConfig, OrderSerializerConfig, OrderItemsSerializerConfig

class CustomPagination(PageNumberPagination):
    page_size = 5



class CommentsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    serializer_class = OrderSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination


class OrderItemsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination
