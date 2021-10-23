from django.urls import path

from bloodbank.views import UpdateBloodBank
from configuration.views import UpdateConfig

app_name = 'configuration'

urlpatterns = [
    # path('list/', ListBloodBank.as_view(), name='ListBloodBank'),
    # path('add/', AddBloodBank.as_view(), name='AddBloodBank'),
    path('update/<int:pk>', UpdateConfig.as_view(), name='UpdateConfig'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]