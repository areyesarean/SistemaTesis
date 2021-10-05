from django.forms import *

from consultorio.models import Consultorio
from donante.models import Donante


class FormDonante(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Donante
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'ci': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Carnet de identidad',
            }),
            'nombre': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }),
            'apellidos': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Primer y Segundo Apellido',
            }),
            'edad': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': '18',
                'max': '70'
            }),
            'direccion': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Direccion particular',
                'row': '12'
            }),
            'consultorio': Select(attrs={
                'class': 'form-control select2'
            }),
            'bloodgroup': Select(attrs={
                'class': 'form-control select2'
            }),
            'sexo': Select(attrs={
                'class': 'form-control select2'
            }),
            'skincolor': Select(attrs={
                'class': 'form-control select2'
            }),

        }

class Consultorio2(Form):
    consultorio = ModelChoiceField(queryset=Consultorio.objects.all(), widget=Select(attrs={
        'class': 'form-control select2'
    }))