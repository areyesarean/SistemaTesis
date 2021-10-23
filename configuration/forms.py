from django.forms import ModelForm, NumberInput

from configuration.models import Configuration


class FormConfiguration(ModelForm):
    class Meta:
        model = Configuration
        fields = '__all__'
        widgets = {
            'don_mensu': NumberInput(attrs={
                'class': 'form-control touchpin text-center',
                'placeholder': 'Número del Consultorio',

            })}
