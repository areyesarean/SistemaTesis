from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import TemplateView

from areasalud.models import AreaSalud
from bloodbank.models import BloodBank
from configuration.models import Configuration
from consultorio.models import Consultorio
from core.models import Estudiante, Municipio
from donacion.models import Donacion
from donante.models import Donante
from sexo.models import Sexos


class MenuPpal(LoginRequiredMixin, TemplateView):
    template_name = 'interfaz/graficos.html'
    def create_config(self):
        if not Configuration.objects.count() == 1:
            print('Configuration create successful')
            Configuration(pk=1, don_mensu=3).save()
            return 1

    def graphic_sexo(self):
        data = []
        for i in Sexos.objects.all():
            data.append({
                'name': i.sexo,
                'y': Donante.objects.filter(sexo__sexo=i).count()
            })
        return data

    def graphic_catMunicipio(self):
        data = []
        for i in AreaSalud.objects.all():
            data.append(Donante.objects.filter(consultorio__areasalud=i).count())
        return data

    def get_municipios(self):
        data = []
        for i in Municipio.objects.all():
            data.append(i.municipio)
        return data

    def get_areasalud(self):
        data = []
        for i in AreaSalud.objects.all():
            data.append(i.nombre)
        return data

    def cant_estudiantes(self):
        return Estudiante.objects.count()

    def cant_donaciones(self):
        return Donacion.objects.count()

    def get_context_data(self, **kwargs):
        context = super(MenuPpal, self).get_context_data(**kwargs)
        context['title'] = 'Página Principal'
        context['data'] = self.graphic_sexo()
        context['municipios'] = self.get_municipios()
        context['areasalud'] = self.get_areasalud()
        context['cant_areasalud'] = AreaSalud.objects.count()
        context['cant_blood_bank'] = BloodBank.objects.count()
        context['cant_donantes'] = Donante.objects.count()
        context['cant_consultorios'] = Consultorio.objects.count()
        context['data_municipios'] = self.graphic_catMunicipio()
        context['cant_estudiantes'] = self.cant_estudiantes()
        context['cant_donaciones'] = self.cant_donaciones()
        context['config'] = self.create_config()
        return context
