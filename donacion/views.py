from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView, UpdateView

from donacion.forms import FormDonacion, FormSearchDonante, FormFilterDonacion, FormDonacionUpdate
from donacion.models import Donacion
from donante.models import Donante


class AddDonacion(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'donacion.add_donacion'
    form_class = FormDonacion
    template_name = 'donacion/Add_Donacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = []
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                donante = Donante.objects.get(ci__exact=request.POST['ci'])
                data.append(donante.toJson())
            elif action == 'add':
                print(request.POST)
                print(self.get_form())
                form = FormDonacion(request.POST)
                form.save()
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de evaluación'
        context['formSearch'] = FormSearchDonante
        return context


class ListDonacion(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ['donacion.delete_donacion', 'donacion.view_donacion']
    template_name = 'donacion/List_Donacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                donaciones = Donacion.objects.all()
                if len(start_date) and len(end_date):
                    donaciones = donaciones.filter(fecha__range=[start_date, end_date])
                for i in donaciones:
                    data.append(i.toJson())
            elif action == 'del-mult':
                if request.user.is_superuser:
                    for i in request.POST.getlist('ids[]'):
                        est = Donacion.objects.get(pk=i)
                        est.delete()
                else:
                    data['error'] = 'No tiene permisos para realizar esta acción'
            elif action == 'del':
                if request.user.is_superuser:
                    est = Donacion.objects.get(pk=request.POST['id'])
                    est.delete()
                else:
                    data['error'] = 'No tiene permisos para realizar esta acción'
            else:
                data['error'] = 'No hay action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListDonacion, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Donaciones'
        context['formFilter'] = FormFilterDonacion
        return context


class UpdateDonacion(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'donacion.change_donacion'
    template_name = 'donacion/Update_Donacion.html'
    form_class = FormDonacionUpdate
    success_url = reverse_lazy('consultorio:ListConsultorio')
    model = Donacion

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateDonacion, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.user.is_superuser:
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Usted no tiene permisos para realizar esta acción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UpdateDonacion, self).get_context_data(**kwargs)
        context['title'] = 'Editar Donación'
        context['action'] = 'edit'
        context['formSearch'] = FormSearchDonante
        context['data'] = Donante.objects.get(ci__exact=self.object.toJson()['donante']).toJson()
        return context
