from django.urls import path

from bloodbank.views import ListBloodBank, AddBloodBank, UpdateBloodBank

app_name = 'bloodbank'

urlpatterns = [
    path('list/', ListBloodBank.as_view(), name='ListBloodBank'),
    path('add/', AddBloodBank.as_view(), name='AddBloodBank'),
    path('update/<int:pk>', UpdateBloodBank.as_view(), name='UpdateBloodBank'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
