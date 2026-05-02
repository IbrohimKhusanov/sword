from django_filters import rest_framework as django_filters  #pip install django-filter
from django.contrib.auth import get_user_model

User = get_user_model()



class UserFilter(django_filters.FilterSet):
    phone_number = django_filters.CharFilter(field_name="phone_number", lookup_expr='icontains')
    email = django_filters.CharFilter(field_name="email", lookup_expr='icontains')
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr='icontains')
    address = django_filters.CharFilter(field_name="address", lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(field_name="is_active")
    is_staff = django_filters.BooleanFilter(field_name="is_staff")

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'first_name', 'address', 'is_active', 'is_staff']