# Create your views here.
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from areasalud.models import AreaSalud
from bloodgroup.models import BloodGroup
from configuration.models import Configuration
from consultorio.models import Consultorio
from donacion.models import Donacion
from municipio.models import Municipios
from reportes.forms import FormYears, FormRPC, FormRPDiario, FormReportMonth, FormRPAnualMun


# Reporte menu
class ReportesMenuView(TemplateView):
    template_name = 'reportes/Reportes_Menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes'
        return context


# Reporte anual
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


# reporte donaciones de consultorios por area de salud
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


# reporte diario por area de salud
class ReportesResultadoDiarioView(TemplateView):
    template_name = 'reportes/reporte_diario.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ReportesResultadoDiarioView, self).dispatch(request, *args, **kwargs)

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
                fecha = request.POST.get('fecha', '')
                if len(id_area) and len(fecha):
                    for i in Consultorio.objects.filter(areasalud_id=id_area):
                        data.append({
                            'name': i.numero,
                            'y': Donacion.objects.filter(consultorio_id=i.pk, fecha=fecha).count()
                        })

            elif action == 'show_data':
                data = []
                don_consu = []
                fecha = request.POST.get('fecha', '')
                id_area = request.POST.get('id_area', '')
                cant_don = Donacion.objects.filter(consultorio__areasalud=id_area, fecha=fecha).count()
                donaciones = []

                for consu in Consultorio.objects.filter(areasalud_id=id_area):
                    donaciones.append({
                        'consu': consu.numero,
                        'cant_don': Donacion.objects.filter(consultorio_id=consu, consultorio__areasalud=id_area,
                                                            fecha=fecha).count()
                    })
                data.append({
                    'cant_don': cant_don,
                    'don_consu': donaciones
                })
            elif action == 'list_cant':
                data = []
                fecha = request.POST.get('fecha', '')
                id_area = request.POST.get('id_area', '')

                for consu in Consultorio.objects.filter(areasalud_id=id_area):
                    data.append({
                        'numero': consu.numero,
                        'direccion': consu.direccion,
                        'cant_don': Donacion.objects.filter(consultorio_id=consu, consultorio__areasalud=id_area,
                                                            fecha=fecha).count()
                    })
            elif action == 'show_graphic_blood_group':
                data = []
                id_area = request.POST.get('id_area', '')
                fecha = request.POST.get('fecha', '')
                if len(id_area) and len(fecha):
                    for blood_group in BloodGroup.objects.all():
                        data.append({
                            'name': blood_group.bloodgroup,
                            'y': Donacion.objects.filter(consultorio__areasalud=id_area, fecha=fecha,
                                                            donante__bloodgroup=blood_group).count()
                        })

                    print(data)
            else:
                data['error'] = 'No se especificó un action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultado Diario por area de salud'
        context['FormRPC'] = FormRPDiario
        return context


# Reporte mesnual
class ReportesResultadoMensualView(TemplateView):
    template_name = 'reportes/Reportes_Resultado_Mensual.html'

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
                month = request.POST.get('month', '')
                municipio = request.POST.get('municipios', '')
                cant_don_con_mes = Configuration.objects.get(pk=1)

                if len(year) and len(municipio):
                    consultorios = Consultorio.objects.filter(areasalud__municipio_id=municipio)
                    if not len(consultorios):
                        raise ValueError(
                            'Uyy, No existen consultorios asociados al municipio seleccionado en el año seleccionado en el mes seleccionado')

                    cant_consul = consultorios.count()
                    donaciones_previstas = (cant_consul * cant_don_con_mes.don_mensu)
                    cons_sobre = 0
                    cons_cump = 0
                    cons_incum = 0

                    cons_incum_data = []
                    cons_cump_data = []
                    cons_sobre_data = []

                    for i in consultorios:
                        cant = Donacion.objects.filter(consultorio__numero=i.numero, fecha__year=year,
                                                       fecha__month=month).count()
                        if cant > cant_don_con_mes.don_mensu:
                            cons_sobre_data.append(i.toJson())
                            cons_cump_data.append(i.toJson())
                            cons_sobre += 1
                            cons_cump += 1
                        elif cant < cant_don_con_mes.don_mensu:
                            cons_incum_data.append(i.toJson())
                            cons_incum += 1
                        else:
                            cons_cump_data.append(i.toJson())
                            cons_cump += 1

                    donaciones = Donacion.objects.filter(fecha__year=year, fecha__month=month,
                                                         bloodbank__municipio_id=municipio)
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
                            "Uyy, No hay donaciones asociadas al municipio seleccionado en el año seleccionado en el mes seleccionado")
            else:
                data['error'] = 'No hay action'
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultado Anual'
        context['FormYears'] = FormReportMonth
        return context


# Reprote diario por municipio
class ReportesResultadoDiarioMunView(TemplateView):
    template_name = 'reportes/reporte_diario_mun.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ReportesResultadoDiarioMunView, self).dispatch(request, *args, **kwargs)

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
                id_mun = request.POST.get('id_mun', '')
                fecha = request.POST.get('fecha', '')
                if len(id_mun) and len(fecha):
                    for i in Consultorio.objects.filter(areasalud__municipio_id=id_mun):
                        data.append({
                            'name': i.numero,
                            'y': Donacion.objects.filter(consultorio_id=i.pk, fecha=fecha).count()
                        })
            elif action == 'show_data':
                data = []
                don_consu = []
                fecha = request.POST.get('fecha', '')
                id_mun = request.POST.get('id_mun', '')
                cant_don = Donacion.objects.filter(consultorio__areasalud__municipio_id=id_mun, fecha=fecha).count()
                donaciones = []

                for consu in Consultorio.objects.filter(areasalud__municipio_id=id_mun):
                    donaciones.append({
                        'consu': consu.numero,
                        'cant_don': Donacion.objects.filter(consultorio_id=consu,
                                                            consultorio__areasalud__municipio_id=id_mun,
                                                            fecha=fecha).count()
                    })
                data.append({
                    'cant_don': cant_don,
                    'don_consu': donaciones
                })
            elif action == 'list_cant':
                data = []
                fecha = request.POST.get('fecha', '')
                id_mun = request.POST.get('id_mun', '')

                for consu in Consultorio.objects.filter(areasalud__municipio_id=id_mun):
                    data.append({
                        'numero': consu.numero,
                        'direccion': consu.direccion,
                        'cant_don': Donacion.objects.filter(consultorio_id=consu,
                                                            consultorio__areasalud__municipio_id=id_mun,
                                                            fecha=fecha).count()
                    })
            elif action == 'show_graphic_blood_group':
                data = []
                id_mun = request.POST.get('id_mun', '')
                print(id_mun)
                fecha = request.POST.get('fecha', '')
                if len(id_mun) and len(fecha):
                    for blood_group in BloodGroup.objects.all():
                        data.append({
                            'name': blood_group.bloodgroup,
                            'y': Donacion.objects.filter(consultorio__areasalud__municipio_id=id_mun, fecha=fecha,
                                                            donante__bloodgroup=blood_group).count()
                        })

                    print(data)
            else:
                data['error'] = 'No se especificó un action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Resultado Diario por municipio'
        context['FormRPC'] = FormRPDiario
        return context


# Es el reprote anual con el grafioc de linia
class ReporteComportamientoAnualDonaciones(TemplateView):
    template_name = 'reportes/reporte_anual_don_municipio.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ReporteComportamientoAnualDonaciones, self).dispatch(request, *args, **kwargs)

    def graphic_comp_men_mun(self, mun, year):
        try:
            mont = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            data = []
            cant_don_year = []
            for area in AreaSalud.objects.filter(municipio_id=mun):
                for mes in mont:
                    cant_don_year.append(
                        Donacion.objects.filter(fecha__year=year, fecha__month=mes,
                                                consultorio__areasalud=area.pk).count())
                data.append({
                    'name': area.nombre,
                    'data': cant_don_year
                })
                cant_don_year = []

            print('GRAFICO LINIA')
            print(data)
            return data
        except Exception as e:
            return JsonResponse({'error': str(e)})

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
                id_mun = request.POST.get('id_mun', '')
                year = request.POST.get('year', '')
                mun_name = Municipios.objects.get(pk=id_mun).toJson()

                if len(id_mun) and len(year):
                    data.append({
                        'mun_name': mun_name['municipio'],
                        'graphic': self.graphic_comp_men_mun(id_mun, year)
                    })
            else:
                data['error'] = 'No se especificó un action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Comportamiento anual de donaciones'
        context['FormRPC'] = FormRPAnualMun
        return context
