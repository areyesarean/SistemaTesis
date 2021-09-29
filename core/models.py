from crum import get_current_user
from django.db import models
from django.forms import model_to_dict
from core import mchoices
from .validators import CI_VALIDATORS, EDAD_VALIDATORS


class Auditoria(models.Model):
    created_by = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, blank=True,
                                   related_name='created_by')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_by = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, blank=True,
                                    related_name='modified_by')
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Sexo(models.Model):
    sexo = models.CharField('Sexo', unique=True, choices=mchoices.sexo, max_length=9)

    def __str__(self):
        return self.sexo

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        # ordering = ['sexo']


class Provincia(models.Model):
    provincia = models.CharField('Provincia', unique=True, choices=mchoices.Provincias, max_length=20)

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        # ordering = ['provincia']


class Municipio(models.Model):
    municipio = models.CharField('Municipio', unique=True, max_length=20)

    def __str__(self):
        return self.municipio

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        # ordering = ['municipio']


class Estudiante(Auditoria):
    ci = models.CharField('Carnet de identidad', max_length=11, unique=True, validators=CI_VALIDATORS)
    nombre = models.CharField('Nombre', max_length=50)
    edad = models.PositiveIntegerField('Edad', name='age', validators=EDAD_VALIDATORS)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT, verbose_name='Sexo')
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, verbose_name='Provincia')
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Municipio')

    def __str__(self):
        return self.nombre

    def toJson(self):
        item = model_to_dict(self)
        item['sexo'] = self.sexo.sexo
        item['provincia'] = self.provincia.provincia
        item['municipio'] = self.municipio.municipio
        return item

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.created_by = user
            else:
                self.modified_by = user
        super(Estudiante, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        # ordering = ['id']
