from django.db import models

# Create your models here.
from django.forms import model_to_dict


class Configuration(models.Model):
    don_mensu = models.IntegerField(verbose_name='Cantidad de Donaciones Mensuales', default=3)

    def __str__(self):
        return '{}'.format(self.don_mensu)

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        return item