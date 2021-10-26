from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from areasalud.forms import FormAreaSalud
from areasalud.models import AreaSalud


class ListAreaSalud(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'areasalud.view_areasalud'
    template_name = 'areasalud/List_Areasalud.html'
    model = AreaSalud

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListAreaSalud, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in AreaSalud.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = AreaSalud.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = AreaSalud.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListAreaSalud, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Áreas de Salud'
        context['btnadd'] = 'Crear nueva Área de Salud'
        return context


class AddAreaSalud(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'areasalud.add_areasalud'
    template_name = 'areasalud/AddAreasalud.html'
    form_class = FormAreaSalud
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
        context = super(AddAreaSalud, self).get_context_data(**kwargs)
        context['title'] = 'Crear nueva Área de Salud'
        return context


class UpdateAreaSalud(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'areasalud.change_areasalud'
    template_name = 'areasalud/AddAreasalud.html'
    form_class = FormAreaSalud
    success_url = reverse_lazy('areasalud:ListAreaSalud')
    model = AreaSalud

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateAreaSalud, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateAreaSalud, self).get_context_data(**kwargs)
        context['title'] = 'Editar Área de Salud'
        return context
