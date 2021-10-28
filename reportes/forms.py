from datetime import datetime

from django.forms import *

from municipio.models import Municipios
from provincia.models import Provincias


class FormYears(Form):
    years = IntegerField(label='Seleccione el año', widget=NumberInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': datetime.now().year,
    }))

    municipios = ModelChoiceField(queryset=Municipios.objects.all(), label='Seleccione el municipio',
                                  widget=Select(attrs={
                                      'class': 'form-control select2'
                                  }))

class FormRPC(Form):
    years = IntegerField(label='Seleccione el año', widget=NumberInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': datetime.now().year,
    }))
    provincia = ModelChoiceField(queryset=Provincias.objects.all(), label='Seleccione la Provincia',
                                 widget=Select(attrs={
                                     'class': 'form-control select2'
                                 }))
    municipios = CharField(label='Seleccione el Municipio',
                           widget=Select(attrs={
                               'class': 'form-control select2'
                           }))

    areasalud = CharField(label='Seleccione el Área de Salud',
                          widget=Select(attrs={
                              'class': 'form-control select2'
                          }))

class FormRPDiario(Form):
    fecha = CharField(label='Seleccione la fecha',
                      widget=TextInput(attrs={
                          'class': 'form-control',
                          'autocomplete': 'off'
                      }))
    provincia = ModelChoiceField(queryset=Provincias.objects.all(), label='Seleccione la Provincia',
                                 widget=Select(attrs={
                                     'class': 'form-control select2'
                                 }))
    municipios = CharField(label='Seleccione el Municipio',
                           widget=Select(attrs={
                               'class': 'form-control select2'
                           }))

    areasalud = CharField(label='Seleccione el Área de Salud',
                          widget=Select(attrs={
                              'class': 'form-control select2'
                          }))

class FormReportMonth(Form):
    years = IntegerField(label='Seleccione el año', widget=NumberInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': datetime.now().year,
    }))

    municipios = ModelChoiceField(queryset=Municipios.objects.all(), label='Seleccione el municipio',
                                  widget=Select(attrs={
                                      'class': 'form-control select2'
                                  }))

class FormRPAnualMun(Form):
    year = IntegerField(label='Seleccione el año', widget=NumberInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': datetime.now().year,
    }))
    provincia = ModelChoiceField(queryset=Provincias.objects.all(), label='Seleccione la Provincia',
                                 widget=Select(attrs={
                                     'class': 'form-control select2'
                                 }))
    municipios = CharField(label='Seleccione el Municipio',
                           widget=Select(attrs={
                               'class': 'form-control select2'
                           }))
