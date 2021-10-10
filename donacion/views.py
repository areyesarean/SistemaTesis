from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, CreateView

from donacion.forms import FormDonacion, FormSearchDonante
from donante.models import Donante


class AddDonacion(FormView):
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


class AddDonacionP(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'municipios.add_municipios'
    template_name = 'donacion/Add_Donacionssss.html'
    form_class = FormDonacion
    success_url = reverse_lazy('municipio:AddMunicipio')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['action']:
                action = request.POST['action']
                if action == 'search':
                    data = []
                    donante = Donante.objects.get(ci__exact=request.POST['ci'])
                    data.append(donante.toJson())

            form = self.get_form()
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AddDonacionP, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Municipio'
        context['formSearch'] = FormSearchDonante
        return context