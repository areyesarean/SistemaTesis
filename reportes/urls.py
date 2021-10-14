from django.urls import path

from reportes.views import ReportesMenuView, ReportesResultadoAnualView
from sexo.views import ListSexo, AddSexo, UpdateSexo

app_name = 'reportes'

urlpatterns = [
    path('list/', ListSexo.as_view(), name='ListSexo'),
    path('add/', AddSexo.as_view(), name='AddSexo'),
    path('update/<int:pk>', UpdateSexo.as_view(), name='UpdateSexo'),

    path('menu/', ReportesMenuView.as_view(), name='ReportesMenu'),
    path('year/', ReportesResultadoAnualView.as_view(), name='ReportesResultadoAnual'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
    # path('select2/', Plugins.as_view(), name='Plugins'),
    # path('evaluacion/', EvaluacionView.as_view(), name='Evaluacion'),
]
