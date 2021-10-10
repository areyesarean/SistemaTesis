from django.urls import path

from consultorio.views import ListConsultorio, UpdateConsultorio
from donacion.views import AddDonacion, AddDonacionP

app_name = 'donacion'

urlpatterns = [
    path('list/', ListConsultorio.as_view(), name='ListDonacion'),
    path('add/', AddDonacion.as_view(), name='AddDonacion'),
    path('adds/', AddDonacionP.as_view(), name='AddDonacionP'),
    path('update/<int:pk>', UpdateConsultorio.as_view(), name='UpdateDonacion'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
