from django.urls import path

from municipio.views import ListMunicipio, AddMunicipio, UpdateMunicipio

app_name = 'municipio'

urlpatterns = [
    path('list/', ListMunicipio.as_view(), name='ListMunicipio'),
    path('add/', AddMunicipio.as_view(), name='AddMunicipio'),
    path('update/<int:pk>', UpdateMunicipio.as_view(), name='UpdateMunicipio'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
