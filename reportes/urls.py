from django.urls import path

from reportes.views import ReportesMenuView, ReportesResultadoAnualView, \
    Reporte_Donaciones_de_Consultorios_Por_Area_Salud, ReportesResultadoDiarioView, ReportesResultadoMensualView, \
    ReportesResultadoDiarioMunView

app_name = 'reportes'

urlpatterns = [
    path('menu/', ReportesMenuView.as_view(), name='ReportesMenu'),
    path('year/', ReportesResultadoAnualView.as_view(), name='ReportesResultadoAnual'),
    path('day/', ReportesResultadoDiarioView.as_view(), name='ReportesResultadoDiarioView'),
    path('daymun/', ReportesResultadoDiarioMunView.as_view(), name='ReportesResultadoDiarioMunView'),
    path('month/', ReportesResultadoMensualView.as_view(), name='ReportesResultadoMensualView'),
    path('consu/', Reporte_Donaciones_de_Consultorios_Por_Area_Salud.as_view(), name='ReportesDonacionesConsultorio'),

]
