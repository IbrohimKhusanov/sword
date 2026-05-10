from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets, status
from django_filters import rest_framework as django_filters
from rest_framework import filters

from products.filters.product_filter import CategoryFilter, ProductFilter

from products.models import Product, Category, Images
from products.serializers import ProductSerializerConfig, CategorySerializerConfig, ImagesSerializerConfig
from products.permissions import IsStaffOrReadOnly
class CustomPagination(PageNumberPagination):
    page_size = 5



class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = CategoryFilter
    search_fields = ['name']
    pagination_class = CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializerConfig
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'size', 'price']
    pagination_class = CustomPagination

class ImagesViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    queryset = Images.objects.all()
    serializer_class = ImagesSerializerConfig
    # filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    # filterset_class = ProductFilter
    # search_fields = ['name', 'description', 'size', 'price']
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('image')

        product_id = request.data.get('product')
        comment_id = request.data.get('comment')
        service_id = request.data.get('service')

        created = []
        for image in images:
            serializer = self.get_serializer(data={
                'image': image,
                'product': product_id,
                'comment': comment_id,
                'service': service_id
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created.append(serializer.data)

        return Response(created, status=status.HTTP_201_CREATED)  # ← shu yoq

