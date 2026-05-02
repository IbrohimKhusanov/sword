from django_filters import rest_framework as django_filters  #pip install django-filter
from products.models import Comments, Services, OrderItems, Order, ContactLink



class CommentsFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name="user__id")
    product = django_filters.NumberFilter(field_name="product__id")
    comment = django_filters.CharFilter(field_name="comment", lookup_expr='icontains')
    rating_min = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_max = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='exact')

    class Meta:
        model = Comments
        fields = ['user', 'product', 'comment', 'rating']



class OrderFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name="user__id")
    phone_number = django_filters.CharFilter(field_name="phone_number", lookup_expr='icontains')
    total_price_min = django_filters.NumberFilter(field_name='total_price', lookup_expr='gte')
    total_price_max = django_filters.NumberFilter(field_name='total_price', lookup_expr='lte')
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    total_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='exact')

    class Meta:
        model = Order
        fields = ['user', 'phone_number', 'status', 'total_price']



class OrderItemsFilter(django_filters.FilterSet):
    order = django_filters.NumberFilter(field_name="order__id")
    product = django_filters.NumberFilter(field_name="product__id")
    address = django_filters.CharFilter(field_name="address", lookup_expr='icontains')
    quantity_min = django_filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity_max = django_filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    quantity = django_filters.NumberFilter(field_name='quantity', lookup_expr='exact')
    price_at_purchase = django_filters.NumberFilter(field_name='price_at_purchase', lookup_expr='exact')

    class Meta:
        model = OrderItems
        fields = ['order', 'product', 'address', 'quantity', 'price_at_purchase']


class ServicesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    description = django_filters.CharFilter(field_name="description", lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='exact')

    contact_type = django_filters.CharFilter(field_name='contacts__contact_type', lookup_expr='exact')
    contact_value = django_filters.CharFilter(field_name='contacts__value', lookup_expr='icontains')

    class Meta:
        model = Services
        fields = ['name', 'description', 'price']



class ContactLinkFilter(django_filters.FilterSet):
    service = django_filters.NumberFilter(field_name="service__id")
    service_name = django_filters.CharFilter(field_name="service__name", lookup_expr='icontains')
    contact_type = django_filters.CharFilter(field_name='contact_type', lookup_expr='exact')
    value = django_filters.CharFilter(field_name='value', lookup_expr='icontains')

    class Meta:
        model = ContactLink
        fields = ['service', 'contact_type', 'value']
