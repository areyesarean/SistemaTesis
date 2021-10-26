from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from provincia.forms import FormProvincia
from provincia.models import Provincias


class ListProvincia(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'provincia.view_provincias'
    template_name = 'provincia/List_Provincia.html'
    model = Provincias

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListProvincia, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in Provincias.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = Provincias.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = Provincias.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListProvincia, self).get_context_data(**kwargs)
        context['title'] = 'Listado de provincias'
        context['btnadd'] = 'Crear nuevo estudiante'
        return context


class AddProvincia(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'provincia..add_provincia'
    template_name = 'provincia/AddProvincia.html'
    form_class = FormProvincia
    success_url = reverse_lazy('provincia:AddProvincia')

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
        context = super(AddProvincia, self).get_context_data(**kwargs)
        context['title'] = 'Crear nueva Provincia'
        return context


class UpdateProvincia(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'provincia.add_provincia'
    template_name = 'provincia/AddProvincia.html'
    form_class = FormProvincia
    success_url = reverse_lazy('provincia:ListProvincia')
    model = Provincias

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateProvincia, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateProvincia, self).get_context_data(**kwargs)
        context['title'] = 'Editar Provincia'
        return context
