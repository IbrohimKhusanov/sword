from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from django_filters import rest_framework as django_filters

from products.models import Services
from products.serializers import ServicesSerializerConfig

class CustomPagination(PageNumberPagination):
    page_size = 5



class ServicesViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination
