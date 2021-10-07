from django.urls import path

from skincolor.views import UpdateSkinColor, AddSkinColor, ListSkinColor

app_name = 'skincolor'

urlpatterns = [
    path('list/', ListSkinColor.as_view(), name='ListSkinColor'),
    path('add/', AddSkinColor.as_view(), name='AddSkinColor'),
    path('update/<int:pk>', UpdateSkinColor.as_view(), name='UpdateSkinColor'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
    # path('select2/', Plugins.as_view(), name='Plugins'),
    # path('evaluacion/', EvaluacionView.as_view(), name='Evaluacion'),
]
