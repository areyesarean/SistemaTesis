from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView

from core.models import Estudiante, Sexo, Municipio


class MenuPpal(LoginRequiredMixin, TemplateView):
    template_name = 'interfaz/graficos.html'

    def graphic_sexo(self):
        data = []
        for i in Sexo.objects.all():
            data.append({
                'name': i.sexo,
                'y': Estudiante.objects.filter(sexo__sexo=i).count()
            })
        return data

    def graphic_catMunicipio(self):
        data = []
        for i in Municipio.objects.all():
            data.append(Estudiante.objects.filter(municipio__municipio=i).count())
        return data

    def get_municipios(self):
        data = []
        for i in Municipio.objects.all():
            data.append(i.municipio)
        return data

    def cant_estudiantes(self):
        return Estudiante.objects.count()

    def get_context_data(self, **kwargs):
        context = super(MenuPpal, self).get_context_data(**kwargs)
        context['title'] = 'Página Principal'
        context['data'] = self.graphic_sexo()
        context['municipios'] = self.get_municipios()
        context['data_municipios'] = self.graphic_catMunicipio()
        context['cant_estudiantes'] = self.cant_estudiantes()
        return context