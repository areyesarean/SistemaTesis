from django.forms import ModelForm, TextInput, Select

from provincia.models import Provincias


class FormProvincia(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = Provincias
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'provincia': Select(attrs={
                'class': 'form-control select2'
            }),

        }