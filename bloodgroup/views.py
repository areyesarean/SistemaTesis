from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from areasalud.models import AreaSalud
from bloodgroup.forms import FormBloodGroup
from bloodgroup.models import BloodGroup


class ListBloodGroup(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'bloodgroup.view_bloodgroup'
    template_name = 'bloodgroup/List_BloodGroup.html'
    model = BloodGroup

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListBloodGroup, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in BloodGroup.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = BloodGroup.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = BloodGroup.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListBloodGroup, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Grupos Sanguíneos'
        context['btnadd'] = 'Crear nuevo Grupo Sanguíneo'
        return context


class AddBloodGroup(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'bloodgroup.add_bloodgroup'
    template_name = 'bloodgroup/Add_BloodGroup.html'
    form_class = FormBloodGroup
    success_url = reverse_lazy('areasalud:AddAreaSalud')

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
        context = super(AddBloodGroup, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Grupo Sanguíneo'
        return context


class UpdateBloodGroup(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'bloodgroup.change_bloodgroup'
    template_name = 'bloodgroup/Add_BloodGroup.html'
    form_class = FormBloodGroup
    success_url = reverse_lazy('bloodgroup:ListBloodGroup')
    model = BloodGroup

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateBloodGroup, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateBloodGroup, self).get_context_data(**kwargs)
        context['title'] = 'Editar Grupo Sanguíneo'
        return context
