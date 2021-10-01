from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from municipio.forms import FormMunicipio
from municipio.models import Municipios


class ListMunicipio(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'municipio.view_municipios'
    template_name = 'municipio/List_Municipio.html'
    model = Municipios

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListMunicipio, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("Entro a POST")
        data = {}
        action = request.POST['action']
        print(action)
        try:
            if action == 'list':
                data = []
                for i in Municipios.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = Municipios.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = Municipios.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListMunicipio, self).get_context_data(**kwargs)
        context['title'] = 'Listado de municipios'
        context['btnadd'] = 'Crear nuevo municipio'
        return context


class AddMunicipio(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'municipios.add_municipios'
    template_name = 'municipio/AddMunicipio.html'
    form_class = FormMunicipio
    success_url = reverse_lazy('municipio:AddMunicipio')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AddMunicipio, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Municipio'
        return context


class UpdateMunicipio(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'municipios.change_municipios'
    template_name = 'municipio/AddMunicipio.html'
    form_class = FormMunicipio
    success_url = reverse_lazy('municipio:ListMunicipio')
    model = Municipios

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateMunicipio, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UpdateMunicipio, self).get_context_data(**kwargs)
        context['title'] = 'Editar Municipio'
        return context
