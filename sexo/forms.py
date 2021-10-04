from django.forms import ModelForm, Select

from sexo.models import Sexos


class FormSexo(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Sexos
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'sexo': Select(attrs={
                'class': 'form-control select2'
            }),

        }
