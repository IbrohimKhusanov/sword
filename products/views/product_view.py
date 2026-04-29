from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from django_filters import rest_framework as django_filters

from products.models import Product, Category
from products.serializers import ProductSerializerConfig, CategorySerializerConfig

class CustomPagination(PageNumberPagination):
    page_size = 5



class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination
