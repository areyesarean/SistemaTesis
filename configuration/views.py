from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from configuration.forms import FormConfiguration
from configuration.models import Configuration


class UpdateConfig(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'configuration.change_configuration'
    template_name = 'configuration/config_update.html'
    form_class = FormConfiguration
    success_url = reverse_lazy('bloodgroup:ListBloodGroup')
    model = Configuration

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateConfig, self).dispatch(request, *args, **kwargs)

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
        context = super(UpdateConfig, self).get_context_data(**kwargs)
        context['title'] = 'Configuracion'
        return context
