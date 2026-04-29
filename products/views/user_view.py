from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets
from django_filters import rest_framework as django_filters

from django.contrib.auth import get_user_model

from products.serializers import UserSerializerConfig

User = get_user_model()

class CustomPagination(PageNumberPagination):
    page_size = 5



class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = UserFilter
    # search_fields = ['university', 'eslatma_matni', 'qolgan_kun', 'tugash_kun']
    # pagination_class = CustomPagination
