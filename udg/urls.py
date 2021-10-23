"""udg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from redirect import redirectLogin
from udg import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', redirectLogin, name='Redirect'),
    path('login/', include('login.urls')),
    path('dashboard/', include('interfaz.urls')),
    path('estudiante/', include('core.urls')),
    path('provincia/', include('provincia.urls')),
    path('municipio/', include('municipio.urls')),
    path('areasalud/', include('areasalud.urls')),
    path('bloodbank/', include('bloodbank.urls')),
    path('consultorio/', include('consultorio.urls')),
    path('bloodgroup/', include('bloodgroup.urls')),
    path('sexo/', include('sexo.urls')),
    path('skincolor/', include('skincolor.urls')),
    path('donante/', include('donante.urls')),
    path('donacion/', include('donacion.urls')),
    path('reportes/', include('reportes.urls')),
    path('config/', include('configuration.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
