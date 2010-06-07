from restaurants.models import Restaurant
import django_filters

class RestaurantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Restaurant
        fields = ['cuisine', 'name']
