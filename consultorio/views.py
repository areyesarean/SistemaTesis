from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from consultorio.forms import FormConsultorio
from consultorio.models import Consultorio


class ListConsultorio(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'consultorio.view_consultorio'
    template_name = 'consultorio/List_Consultorio.html'
    model = Consultorio

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListConsultorio, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("Entro a POST")
        data = {}
        action = request.POST['action']
        print(action)
        try:
            if action == 'list':
                data = []
                for i in Consultorio.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = Consultorio.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = Consultorio.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListConsultorio, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Consultorios'
        context['btnadd'] = 'Crear nuevo Consultorio'
        return context


class AddConsultorio(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'consultorio.add_consultorio'
    template_name = 'consultorio/AddConsultorio.html'
    form_class = FormConsultorio
    success_url = reverse_lazy('consultorio:AddConsultorio')
    model = Consultorio

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
        context = super(AddConsultorio, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Consultorio'
        context['action'] = 'create'
        return context


class UpdateConsultorio(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'consultorio.change_consultorio'
    template_name = 'consultorio/AddConsultorio.html'
    form_class = FormConsultorio
    success_url = reverse_lazy('consultorio:ListConsultorio')
    model = Consultorio

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateConsultorio, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateConsultorio, self).get_context_data(**kwargs)
        context['title'] = 'Editar Consultorio'
        context['action'] = 'edit'
        return context
