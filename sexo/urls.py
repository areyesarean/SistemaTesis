from django.urls import path

from sexo.views import ListSexo, AddSexo, UpdateSexo

app_name = 'sexo'

urlpatterns = [
    path('list/', ListSexo.as_view(), name='ListSexo'),
    path('add/', AddSexo.as_view(), name='AddSexo'),
    path('update/<int:pk>', UpdateSexo.as_view(), name='UpdateSexo'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
    # path('select2/', Plugins.as_view(), name='Plugins'),
    # path('evaluacion/', EvaluacionView.as_view(), name='Evaluacion'),
]
