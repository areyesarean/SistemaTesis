from django.urls import path, include
from core.views import ListEstudiante, AddEstudiante, UpdateEstudiante, DeleteEstudiante, PdfEstudiantesView, Plugins, \
    EvaluacionView

app_name = 'core'

urlpatterns = [
    path('list/', ListEstudiante.as_view(), name='ListEstudiante'),
    path('add/', AddEstudiante.as_view(), name='AddEstudiante'),
    path('update/<int:pk>', UpdateEstudiante.as_view(), name='UpdateEstudiante'),
    path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
    path('select2/', Plugins.as_view(), name='Plugins'),
    path('evaluacion/', EvaluacionView.as_view(), name='Evaluacion'),
]
