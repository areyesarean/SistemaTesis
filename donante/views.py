# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from bloodbank.forms import FormBloodBank
from bloodbank.models import BloodBank
from donante.forms import FormDonante, Consultorio2
from donante.models import Donante


class ListDonante(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'donante.view_donante'
    template_name = 'donante/List_Donanate.html'
    model = Donante

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListDonante, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in Donante.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = Donante.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = Donante.objects.get(pk=i)
                    est.delete()
            elif action == 'filter_consu':
                data = []
                for i in Donante.objects.filter(consultorio_id=request.POST['id_consu']):
                    data.append(i.toJson())
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListDonante, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Donantes'
        context['btnadd'] = 'Crear nuevo Donantes'
        context['form'] = Consultorio2()
        return context


class AddDonante(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'donante.add_donante'
    template_name = 'donante/Add_Donanate.html'
    form_class = FormDonante
    success_url = reverse_lazy('donante:AddDonante')

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
        context = super(AddDonante, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Donante'
        return context


class UpdateDonante(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'donante.change_donante'
    template_name = 'donante/Add_Donanate.html'
    form_class = FormDonante
    success_url = reverse_lazy('donante:ListDonante')
    model = Donante

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateDonante, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateDonante, self).get_context_data(**kwargs)
        context['title'] = 'Editar Donante'
        return context
