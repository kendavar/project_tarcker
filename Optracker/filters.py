from Optracker.models import optrackertable
import django_filters

class dashFilter(django_filters.FilterSet):
    type_of_opportunity = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = optrackertable
        fields = ['type_of_opportunity',]
