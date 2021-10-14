from datetime import datetime

from django.forms import *

from municipio.models import Municipios


class FormYears(Form):
    years = IntegerField(label='Seleccione el año', widget=NumberInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': datetime.now().year,
    }))

    municipios = ModelChoiceField(queryset=Municipios.objects.all(), label='Seleccione el municipio', widget=Select(attrs={
        'class': 'form-control select2'
    }))
