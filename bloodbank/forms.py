from django.forms import *

from bloodbank.models import BloodBank


class FormBloodBank(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = BloodBank
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'municipio': Select(attrs={
                'class': 'form-control select2'
            }),
            'nombre': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del banco de Sangre',
            }),

        }

    def clean(self):
        cleaned_data = super(FormBloodBank, self).clean()
        nombre = cleaned_data.get('nombre')
        municipio = cleaned_data.get('municipio')
        try:
            BloodBank.objects.get(nombre=nombre, municipio=municipio)
        except BloodBank.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(
                'Ya existe un Banco de Sangre en el municipios: {} con el nombre: {}. Sugerencia: Cambie de nombre '.format(municipio, nombre))