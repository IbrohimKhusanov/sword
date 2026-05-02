from django_filters import rest_framework as django_filters  #pip install django-filter
from products.models import Comments, User, Product, Category



class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    description = django_filters.CharFilter(field_name="description", lookup_expr='icontains')

    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='exact')

    qoldiq_min = django_filters.NumberFilter(field_name='qoldiq', lookup_expr='gte')
    qoldiq_max = django_filters.NumberFilter(field_name='qoldiq', lookup_expr='lte')
    qoldiq = django_filters.NumberFilter(field_name='qoldiq', lookup_expr='exact')

    size_min = django_filters.NumberFilter(field_name='size', lookup_expr='gte')
    size_max = django_filters.NumberFilter(field_name='size', lookup_expr='lte')
    size = django_filters.NumberFilter(field_name='size', lookup_expr='exact')

    category = django_filters.NumberFilter(field_name='category__id')
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'qoldiq', 'size']
