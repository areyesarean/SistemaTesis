from django.forms import ModelForm, Select, TextInput

from areasalud.models import AreaSalud


class FormAreaSalud(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = AreaSalud
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'municipio': Select(attrs={
                'class': 'form-control select2'
            }),
            'nombre': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del area de salud',
            }),

        }
