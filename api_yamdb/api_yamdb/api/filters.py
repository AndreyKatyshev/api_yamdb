import django_filters as filters

from api_yamdb.api_yamdb.review.models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    year = filters.NumberFilter(field_name='year')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Title
        fields = '__all__'
