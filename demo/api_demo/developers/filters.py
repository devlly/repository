import django_filters
from .models import Developers

class DevFilter(django_filters.FilterSet):
    skills = django_filters.CharFilter(name='skills', lookup_expr='skills')

    class Meta:
        model = Developers
        fields = ['skills', ]
