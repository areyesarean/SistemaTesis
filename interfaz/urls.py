from django.urls import path

from interfaz.views import MenuPpal

app_name = 'interfaz'

urlpatterns = [
    path('', MenuPpal.as_view(), name='MenuPpal'),
]
