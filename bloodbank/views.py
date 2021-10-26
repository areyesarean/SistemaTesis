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


class ListBloodBank(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'bloodbank.view_bloodbank'
    template_name = 'bloodbank/List_BloodBank.html'
    model = BloodBank

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListBloodBank, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in BloodBank.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = BloodBank.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = BloodBank.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListBloodBank, self).get_context_data(**kwargs)
        context['title'] = 'Listado de Bancos de Sangre'
        context['btnadd'] = 'Crear nuevo Banco de Sangre'
        return context


class AddBloodBank(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'bloodbank.add_bloodbank'
    template_name = 'bloodbank/AddBloodBank.html'
    form_class = FormBloodBank
    success_url = reverse_lazy('bloodbank:AddBloodBank')

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
        context = super(AddBloodBank, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Banco de Sangre'
        return context


class UpdateBloodBank(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'bloodbank.change_bloodbank'
    template_name = 'bloodbank/AddBloodBank.html'
    form_class = FormBloodBank
    success_url = reverse_lazy('bloodbank:ListBloodBank')
    model = BloodBank

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateBloodBank, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateBloodBank, self).get_context_data(**kwargs)
        context['title'] = 'Editar Banco de Sangre'
        return context
