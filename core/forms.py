from datetime import datetime

from django.forms import *

from core.models import Estudiante, Sexo


class FormEstudiante(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Estudiante
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'ci': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Carnet de identidad',
            }),
            'nombre': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre y apellidos',
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad'
            }),
            'sexo': Select(attrs={
                'class': 'form-control select2'
            }),
            'provincia': Select(attrs={
                'class': 'form-control select2'
            }),
            'municipio': Select(attrs={
                'class': 'form-control select2'
            }),
        }

    def clean(self):
        cleaned_data = super(FormEstudiante, self).clean()
        nombre = cleaned_data.get('nombre')
        age = cleaned_data.get('age')
        try:
            Estudiante.objects.get(nombre=nombre, age=age)
        except Estudiante.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('Ya existe un estudiante: {} con edad: {} años'.format(nombre, age))

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data


class Select2(Form):
    sexo = ModelChoiceField(queryset=Sexo.objects.all(), widget=Select(attrs={
        'class': 'form-control select2'
    }))
    estudiantes = CharField(label='Estudiantes dado el sexo', widget=Select(attrs={
        'class': 'form-control select2'
    }))

    Fecha = CharField(widget=TextInput(attrs={
        'class': 'form-control datetimepicker-input',
        'id': 'fecha',
        'autocomplete': 'off',
        'data-target': '#fecha',
        'data-toggle': 'datetimepicker',

    }))

    touchpin = CharField(widget=TextInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': '0.0'
    }))

    range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'range'
    }))


class Evaluacion(Form):
    estudiante = CharField(widget=TextInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Nombre del estudiante',
        'disabled': ''
    }))
    tipo_de_evaluacion = CharField(
        widget=Select(choices=(('', '------------'), ('tc', 'Trabajo de control'), ('pe', 'Pregunta escrita')), attrs={
            'class': 'form-control select2 mb-2',
            'disabled': '',
            'id': 'id_typEval'
        }))
    nota = CharField(widget=TextInput(attrs={
        'class': 'form-control text-center',
        'id': 'touchpin',
        'value': '2',
        'disabled': '',
    }))
    fecha_de_la_evaluacion = DateTimeField(widget=DateTimeInput(attrs={
        'class': 'form-control',
        'id': 'range',
        'value': datetime.now().strftime('%m-%d-%Y'),
        'disabled': '',
        'id': 'id_fechaEval'

    }))
