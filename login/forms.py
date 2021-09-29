from django.contrib.auth.models import User
from django.forms import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email',
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
        }
