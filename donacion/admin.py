from django.contrib import admin

# Register your models here.
from donacion.models import Donacion

class DonacionAdmin(admin.ModelAdmin):
    list_display = ("bloodbank", "donante", "consultorio", "fecha", "observaciones")

admin.site.register(Donacion, DonacionAdmin)