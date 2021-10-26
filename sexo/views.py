from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from sexo.forms import FormSexo
from sexo.models import Sexos


class ListSexo(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'provincia.view_provincias'
    template_name = 'sexo/List_Sexo.html'
    model = Sexos

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListSexo, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in Sexos.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = Sexos.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = Sexos.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListSexo, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Sexos'
        context['btnadd'] = 'Crear nuevo Sexo'
        return context


class AddSexo(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'provincia..add_provincia'
    template_name = 'sexo/Add_Sexo.html'
    form_class = FormSexo
    success_url = reverse_lazy('sexo:AddSexo')

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
        context = super(AddSexo, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Sexo'
        return context


class UpdateSexo(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'provincia.add_provincia'
    template_name = 'sexo/Add_Sexo.html'
    form_class = FormSexo
    success_url = reverse_lazy('sexo:AddSexo')
    model = Sexos

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateSexo, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateSexo, self).get_context_data(**kwargs)
        context['title'] = 'Editar Sexo'
        return context
