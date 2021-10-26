from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from skincolor.forms import FormSkincolor
from skincolor.models import SkinColor


class ListSkinColor(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'skincolor.view_skincolor'
    template_name = 'skincolor/List_Skincolor.html'
    model = SkinColor

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListSkinColor, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in SkinColor.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = SkinColor.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = SkinColor.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListSkinColor, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Color de la piel'
        context['btnadd'] = 'Crear nuevo Color de la piel'
        return context


class AddSkinColor(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'skincolor.add_skincolor'
    template_name = 'skincolor/Add_Skincolor.html'
    form_class = FormSkincolor
    success_url = reverse_lazy('skincolor:AddSkinColor')

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
        context = super(AddSkinColor, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Color de la piel'
        return context


class UpdateSkinColor(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'skincolor.add_skincolor'
    template_name = 'skincolor/Add_Skincolor.html'
    form_class = FormSkincolor
    success_url = reverse_lazy('skincolor:AddSkinColor')
    model = SkinColor

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateSkinColor, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateSkinColor, self).get_context_data(**kwargs)
        context['title'] = 'Editar Color de la piel'
        return context
