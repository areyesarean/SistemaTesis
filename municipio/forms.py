from django.forms import ModelForm, Select, TextInput

from municipio.models import Municipios


class FormMunicipio(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Municipios
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'provincia': Select(attrs={
                'class': 'form-control select2'
            }),
            'municipio': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Municipio',
            }),

        }
