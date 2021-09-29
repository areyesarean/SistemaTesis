from django.contrib import admin

# Register your models here.
from core.models import Sexo, Estudiante, Provincia, Municipio


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id', 'ci', 'nombre', 'age', 'sexo', 'provincia', 'municipio', ]
    search_fields = ['ci', 'nombre', 'age', 'municipio__municipio', 'sexo__sexo', 'provincia__provincia']
    list_filter = ['age', 'sexo', 'municipio']


admin.site.register(Sexo)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Provincia)
admin.site.register(Municipio)
