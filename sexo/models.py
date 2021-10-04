from django.db import models

# Create your models here.
from django.forms import model_to_dict

from sexo import sexo_choices


class Sexos(models.Model):
    sexo = models.CharField('Sexo', unique=True, choices=sexo_choices.sexo, max_length=9)

    def __str__(self):
        return self.sexo

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        # ordering = ['sexo']

    def toJson(self):
        item = model_to_dict(self)
        return item