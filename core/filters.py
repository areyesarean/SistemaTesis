import django_filters as filters
from .models import *


class EstudianteFilter(filters.FilterSet):
    class Meta:
        model = Estudiante
        fields = {
            'ci': ['exact', 'icontains'],
            'name': ['exact', 'icontains']
        }
