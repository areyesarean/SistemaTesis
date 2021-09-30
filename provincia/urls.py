from django.urls import path, include

from provincia.views import ListProvincia, AddProvincia, UpdateProvincia

app_name = 'provincia'

urlpatterns = [
    path('list/', ListProvincia.as_view(), name='ListProvincia'),
    path('add/', AddProvincia.as_view(), name='AddProvincia'),
    path('update/<int:pk>', UpdateProvincia.as_view(), name='UpdateProvincia'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
    # path('select2/', Plugins.as_view(), name='Plugins'),
    # path('evaluacion/', EvaluacionView.as_view(), name='Evaluacion'),
]
