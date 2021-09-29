from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy


class ValidatePermissionRequiredMixin(object):
    permission_required = None
    # Url a donde vamos si no tiene permiso
    url_redirect = None

    # los permisos especificados se convierten a tupla o si es uno a el mismo
    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    # Si no se especifica la url a redireccionar lo mandamos a la pagina principal
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('MenuPpal')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super(ValidatePermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(self.get_url_redirect())
