from django.forms import *

from donacion.models import Donacion


class FormSearchDonante(Form):
    ci = IntegerField(label='Escriba el carnet de identidad del donante', widget=TextInput(attrs={
        'class': 'form-control',
        'maxlength': '11',
        'minlength': '11',
        'placeholder': 'Carnet de identidad',
        'pattern': '[0-9!?-]{8,12}',
        'autocomplete': 'off'
    }))


class FormFilterDonacion(Form):
    filter = CharField(label='Seleccione el filtro', widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'id': 'range',
    }))


class FormDonacion(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Donacion
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {

            'bloodbank': Select(attrs={
                'class': 'form-control select2'
            }),
            'donante': Select(attrs={
                'class': 'form-control select2',
                'hidden': 'true',
                'disabled': 'true'
            }),
            'consultorio': Select(attrs={
                'class': 'form-control select2'
            }),
            'fecha': DateInput(attrs={
                'class': 'form-control datetimepicker-input',
                'placeholder': '',
                'data-target': '#id_fecha',
                'data-toggle': 'datetimepicker'
            }),
            'observaciones': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones',
                'rows': '1'
            }),
        }


class FormDonacionUpdate(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Donacion
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {

            'bloodbank': Select(attrs={
                'class': 'form-control select2'
            }),
            'donante': Select(attrs={
                'class': 'form-control',
                'hidden': 'true',
            }),
            'consultorio': Select(attrs={
                'class': 'form-control select2'
            }),
            'fecha': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'observaciones': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones',
                'rows': '1'
            }),
        }
