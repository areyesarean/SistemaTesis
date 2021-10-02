from django.forms import *

from bloodbank.models import BloodBank
from consultorio.models import Consultorio


class FormConsultorio(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Consultorio
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'areasalud': Select(attrs={
                'class': 'form-control select2'
            }),
            'direccion': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección del consultorio'
            }),
            'numero': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número del Consultorio',
            }),

        }

    def clean(self):
        cleaned_data = super(FormConsultorio, self).clean()
        numero = cleaned_data.get('numero')
        areasalud = cleaned_data.get('areasalud')
        try:
            Consultorio.objects.get(numero=numero, areasalud=areasalud)
        except Consultorio.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(
                'Ya existe un Consultorio en el Área de Salud: "{}" con el número: "{}". <b>Sugerencia: Cambie de número<b/> '.format(areasalud, numero))