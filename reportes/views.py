# Create your views here.

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from areasalud.models import AreaSalud
from configuration.models import Configuration
from consultorio.models import Consultorio
from donacion.models import Donacion
from municipio.models import Municipios
from reportes.forms import FormYears, FormRPC


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
                serie.append(
                    Donacion.objects.filter(fecha__year=year, fecha__month=i, bloodbank__municipio_id=muni.pk).count())

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
                cant_don_con_mes = Configuration.objects.get(pk=1)

                if len(year) and len(municipio):
                    consultorios = Consultorio.objects.filter(areasalud__municipio_id=municipio)
                    if not len(consultorios):
                        raise ValueError(
                            'Uyy, No existen consultorios asociados al municipio seleccionado en el año seleccionado')

                    cant_consul = consultorios.count()
                    donaciones_previstas = (cant_consul * cant_don_con_mes.don_mensu) * 12
                    cons_sobre = 0
                    cons_cump = 0
                    cons_incum = 0

                    cons_incum_data = []
                    cons_cump_data = []
                    cons_sobre_data = []

                    for i in consultorios:
                        cant = Donacion.objects.filter(consultorio__numero=i.numero, fecha__year=year).count()
                        if cant > cant_don_con_mes.don_mensu * 12:
                            cons_sobre_data.append(i.toJson())
                            cons_cump_data.append(i.toJson())
                            cons_sobre += 1
                            cons_cump += 1
                        elif cant < cant_don_con_mes.don_mensu * 12:
                            cons_incum_data.append(i.toJson())
                            cons_incum += 1
                        else:
                            cons_cump_data.append(i.toJson())
                            cons_cump += 1
                    print(cons_sobre_data)

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
                        data.append(cons_incum_data)
                        data.append(cons_sobre_data)
                        data.append(cons_cump_data)
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


class Reporte_Donaciones_de_Consultorios_Por_Area_Salud(TemplateView):
    template_name = 'reportes/Reporte_Comp_Consult.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Reporte_Donaciones_de_Consultorios_Por_Area_Salud, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'mun_in_prov':
                id_prov = request.POST['id']
                data = [{'id': '', 'text': '---------------'}]
                for i in Municipios.objects.filter(provincia__municipios=id_prov):
                    data.append({'id': i.pk, 'text': i.municipio})
            elif action == 'areasalud_in_mun':
                id_mun = request.POST['id']
                data = [{'id': '', 'text': '---------------'}]
                for i in AreaSalud.objects.filter(municipio_id=id_mun):
                    data.append({'id': i.pk, 'text': i.nombre})
            elif action == 'show_graphic':
                data = []
                id_area = request.POST.get('id_area', '')
                year = request.POST.get('year', '')
                if len(id_area) and len(year):
                    for i in Consultorio.objects.filter(areasalud_id=id_area):
                        data.append({
                            'name': i.numero,
                            'y': Donacion.objects.filter(consultorio_id=i.pk, fecha__year=year).count()
                        })
            else:
                data['error'] = 'No se especificó un action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultado Anual por consultorios'
        context['FormRPC'] = FormRPC
        return context
