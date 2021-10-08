from django.urls import path

from consultorio.views import ListConsultorio, AddConsultorio, UpdateConsultorio

app_name = 'donacion'

urlpatterns = [
    path('list/', ListConsultorio.as_view(), name='ListConsultorio'),
    path('add/', AddConsultorio.as_view(), name='AddConsultorio'),
    path('update/<int:pk>', UpdateConsultorio.as_view(), name='UpdateConsultorio'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
