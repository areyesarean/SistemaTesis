from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, UpdateView
from login.forms import UserForm


class LoginTView(LoginView):
    template_name = 'login/login.html'

    @method_decorator(sensitive_post_parameters('username', 'password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('interfaz:MenuPpal')
        return super(LoginTView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginTView, self).get_context_data(**kwargs)
        context['title'] = 'Bienvenido'
        return context


class CerrarSession(LogoutView):
    next_page = reverse_lazy('login:Login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login:Login')
        return super(CerrarSession, self).dispatch(request, *args, **kwargs)


class ChangePassword(LoginRequiredMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'login/PasswordChangeForm.html'

    def get_form(self, form_class=None):
        form = PasswordChangeForm(self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(ChangePassword, self).get_context_data(**kwargs)
        context['title'] = 'Cambiar Contraseña'
        return context


class UdateUSerView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_user'
    model = User
    form_class = UserForm
    template_name = 'login/UpdateUser.html'
    success_url = reverse_lazy('interfaz:MenuPpal')

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.object = request.user
        return super(UdateUSerView, self).dispatch(request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super(UdateUSerView, self).get_context_data(**kwargs)
        context['title'] = 'Editar perfil de usuario'
        return context
