# Create your views here.
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from consultorio.models import Consultorio
from donacion.models import Donacion
from municipio.models import Municipios
from reportes.forms import FormYears


class ReportesMenuView(TemplateView):
    template_name = 'reportes/Reportes_Menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes'
        return context


class ReportesResultadoAnualView(TemplateView):
    template_name = 'reportes/Reportes_Resultado_Anual.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def graphic_comp_men_mun(self, mun, year):
        try:
            mont = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            muni = Municipios.objects.get(pk=mun)
            data = []
            serie = []
            for i in mont:
                serie.append(Donacion.objects.filter(fecha__year=year, fecha__month=i, bloodbank__municipio_id=muni.pk).count())

            print(serie)

            data.append({
                'name': muni.municipio,
                'data': serie
            })
            return data
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']

            if action == 'data_number':

                data = []
                year = request.POST.get('year', '')
                municipio = request.POST.get('municipios', '')



                if len(year) and len(municipio):
                    consultorios = Consultorio.objects.filter(areasalud__municipio_id=municipio)
                    if not len(consultorios):
                        raise ValueError(
                            'Uyy, No existen consultorios asociados al municipio seleccionado en el año seleccionado')

                    cant_consul = consultorios.count()
                    donaciones_previstas = (cant_consul * 3) * 12
                    cons_sobre = 0
                    cons_cump = 0
                    cons_incum = 0

                    for i in consultorios:
                        cant = Donacion.objects.filter(consultorio__numero=i.numero, fecha__year=year).count()
                        if cant > 5:
                            cons_sobre += 1
                        elif cant < 5:
                            cons_incum += 1
                        else:
                            cons_cump += 1

                    donaciones = Donacion.objects.filter(fecha__year=year, bloodbank__municipio_id=municipio)
                    if len(donaciones):
                        data.append({
                            'total_donaciones': donaciones.count(),
                            'total_donaciones_previstas': donaciones_previstas,
                            'porctge_cumplimiento': (donaciones.count() * 100) / donaciones_previstas,
                            'cant_cons_cump': cons_cump,
                            'prctge_cons_cump': (cons_cump * 100) / cant_consul,
                            'cant_cons_incum': cons_incum,
                            'prctge_cons_incum': (cons_incum * 100) / cant_consul,
                            'cant_cons_sobre': cons_sobre,
                            'prctge_cons_sobre': (cons_sobre * 100) / cant_consul,
                        })
                        data.append(self.graphic_comp_men_mun(municipio, year))
                    else:
                        raise ValueError(
                            "Uyy, No hay donaciones asociadas al municipio seleccionado en el año seleccionado")
            else:
                data['error'] = 'No hay action'
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultado Anual'
        context['FormYears'] = FormYears
        return context
