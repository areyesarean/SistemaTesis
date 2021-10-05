from django.urls import path

from donante.views import ListDonante, AddDonante, UpdateDonante

app_name = 'donante'

urlpatterns = [
    path('list/', ListDonante.as_view(), name='ListDonante'),
    path('add/', AddDonante.as_view(), name='AddDonante'),
    path('update/<int:pk>', UpdateDonante.as_view(), name='UpdateDonante'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
