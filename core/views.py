from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, TemplateView, FormView

from core.forms import FormEstudiante, Select2, Evaluacion
from core.models import Estudiante, Sexo

# XhtmlPdf2
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime

from django.contrib import messages
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db import IntegrityError


class ListEstudiante(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'core.view_estudiante'
    template_name = 'core/Estudiante/List_Estudiante.html'
    model = Estudiante

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListEstudiante, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in Estudiante.objects.all():
                    data.append(i.toJson())
            elif action == 'del':
                est = Estudiante.objects.get(pk=request.POST['id'])
                est.delete()
            elif action == 'del-mult':
                for i in request.POST.getlist('ids[]'):
                    est = Estudiante.objects.get(pk=i)
                    est.delete()
            else:
                data['error'] = 'No se especificó una action'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListEstudiante, self).get_context_data(**kwargs)
        context['title'] = 'Listado de estudiantes'
        context['btnadd'] = 'Crear nuevo estudiante'
        return context


class AddEstudiante(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_estudiante'
    template_name = 'core/Add.html'
    form_class = FormEstudiante
    success_url = reverse_lazy('core:AddEstudiante')

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

    # def form_valid(self, form):
    #     try:
    #         estudent = form.save()
    #         messages.success(self.request, 'Estudiante guardado correcamente')
    #     except IntegrityError:
    #         messages.error(self.request, 'Ya existe un estudiante con esos datos')
    #     return super(AddEstudiante, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AddEstudiante, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo estudiante'
        return context


class UpdateEstudiante(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_user'
    template_name = 'core/Add.html'
    form_class = FormEstudiante
    success_url = reverse_lazy('core:ListEstudiante')
    model = Estudiante

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateEstudiante, self).dispatch(request, *args, **kwargs)

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


class DeleteEstudiante(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_estudiante'
    model = Estudiante
    success_url = reverse_lazy('core:ListEstudiante')
    template_name = 'core/estudiante/DelEstudiante.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeleteEstudiante, self).get_context_data(**kwargs)
        context['title'] = 'Confirmación de eliminación de un estudiante'
        return context


class PdfEstudiantesView(View):
    def Cantsexo(self):
        data = []
        for i in Sexo.objects.all():
            data.append({
                'sexo': i.sexo,
                'cant': Estudiante.objects.filter(sexo=i).count()
            })
        return data

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('core/Estudiante/pdfTemplate.html')
            context = {
                'title': 'Listado de estudiantes',
                'data': Estudiante.objects.all().order_by('municipio__municipio'),
                'total': Estudiante.objects.all().count(),
                'sexos': self.Cantsexo(),
                'fecha': datetime.date.today()
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Listado_Estudiantes.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('core:ListEstudiante'))


class Plugins(FormView):
    template_name = 'core/estudiante/plugins.html'
    form_class = Select2

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Plugins, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = []
        try:
            for item in Estudiante.objects.filter(sexo=request.POST['id']):
                data.append({
                    'id': item.id,
                    'text': item.nombre,
                    'data': item.toJson()
                })
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select 2'
        return context


class EvaluacionView(FormView):
    form_class = Evaluacion
    template_name = 'core/Estudiante/evaluacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'list':
                data = []
                for i in Estudiante.objects.all():
                    data.append(i.toJson())
            elif action == 'add':
                form = FormEstudiante(request.POST)
                data = form.save()
            else:
                data['error'] = 'No se ha especficado un action == ?'
        except Exception as e:
            data['error'] = 'Error del try ' + str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de evaluación'
        context['formNew'] = FormEstudiante
        return context
