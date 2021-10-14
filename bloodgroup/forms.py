from django.forms import *

from bloodgroup.models import BloodGroup


class FormBloodGroup(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = BloodGroup
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'bloodgroup': Select(attrs={
                'class': 'form-control select2',
                'placeholder': 'Nombre del Grupo Sanguíneo',
            }),

        }
