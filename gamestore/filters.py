import django_filters
import gamestore.models
from django.db.models import Q

class Game(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Цена от и до')
    available = django_filters.BooleanFilter(method='filter_available', label='В наличии')
    term = django_filters.CharFilter(method='filter_term', label='')
    publisher = django_filters.CharFilter(field_name='publisher__name', label='Издатель')


    class Meta:
        model = gamestore.models.Game
        fields = ['price_range', 'available', 'term', 'publisher']

    def filter_available(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(is_available=True)
        return queryset.filter(is_available=False)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(title__icontains=term) | Q(description__icontains=term)
        return queryset.filter(criteria).distinct()