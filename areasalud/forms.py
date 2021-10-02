from django.forms import *

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

    def clean(self):
        cleaned_data = super(FormAreaSalud, self).clean()
        nombre = cleaned_data.get('nombre')
        municipio = cleaned_data.get('municipio')
        try:
            AreaSalud.objects.get(nombre=nombre, municipio=municipio)
        except AreaSalud.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(
                'Ya existe un Área de Salud en el municipio: {} con el nombre: {}. Sugerencia: Cambie de nombre '.format(
                    municipio, nombre))
