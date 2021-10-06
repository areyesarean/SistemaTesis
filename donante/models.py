from django.db import models

# Create your models here.
from django.forms import model_to_dict

from bloodgroup.models import BloodGroup
from consultorio.models import Consultorio
from core.models import Sexo
from skincolor.models import SkinColor
from .validators import *


class Donante(models.Model):
    ci = models.CharField('Carnet de identidad', unique=True, max_length=11, validators=CI_VALIDATORS, blank=False)
    nombre = models.CharField('Nombre', unique=False, max_length=60, blank=False)
    apellidos = models.CharField('Apellidos', unique=False, max_length=60, blank=False)
    edad = models.IntegerField('Edad', unique=False, validators=EDAD_VALIDATORS, blank=False)
    direccion = models.TextField('Direccion', unique=False, max_length=200, blank=False)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.PROTECT, verbose_name='Consultorio',
                                    related_name='Consultorio')
    bloodgroup = models.ForeignKey(BloodGroup, on_delete=models.PROTECT, verbose_name='Grupo sanguineo',
                                   related_name='BloodGroup')
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT, verbose_name='Sexo', related_name='Sexo')
    skincolor = models.ForeignKey(SkinColor, on_delete=models.PROTECT, verbose_name='Color de la piel',
                                  related_name='SkinColor')

    def __str__(self):
        return '{} - {} {}'.format(self.ci, self.nombre, self.apellidos)

    class Meta:
        verbose_name = 'Donante'
        verbose_name_plural = 'Donantes'
        # ordering = ['municipio']

    def toJson(self):
        item = model_to_dict(self)
        item['consultorio'] = self.consultorio.numero
        item['bloodgroup'] = self.bloodgroup.bloodgroup
        item['areasalud'] = self.consultorio.areasalud.nombre
        item['municipio'] = self.consultorio.areasalud.municipio.municipio
        item['sexo'] = self.sexo.sexo
        item['skincolor'] = self.skincolor.nskincolor
        return item
