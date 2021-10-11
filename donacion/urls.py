from django.urls import path

from donacion.views import AddDonacion, ListDonacion, UpdateDonacion

app_name = 'donacion'

urlpatterns = [
    path('list/', ListDonacion.as_view(), name='ListDonacion'),
    path('add/', AddDonacion.as_view(), name='AddDonacion'),
    path('update/<int:pk>', UpdateDonacion.as_view(), name='UpdateDonacion'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
