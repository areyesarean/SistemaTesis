from django.db import models
from provincia import mchoices


# Create your models here.
class Provincias(models.Model):
    provincia = models.CharField('Provincia', unique=True, choices=mchoices.Provincias, max_length=25)

    def __str__(self):
        return self.provincia

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        # ordering = ['provincia']
