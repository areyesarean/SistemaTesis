from django.forms import ModelForm, Select, TextInput

from skincolor.models import SkinColor


class FormSkincolor(ModelForm):
    error_css_class = 'is-invalid'

    class Meta:
        model = SkinColor
        fields = '__all__'
        exclude = ['created_by', 'modified_by']
        widgets = {
            'nskincolor': TextInput(attrs={
                'class': 'form-control'
            }),

        }
