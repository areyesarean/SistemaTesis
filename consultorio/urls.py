from django.urls import path

from areasalud.views import ListAreaSalud, AddAreaSalud, UpdateAreaSalud

app_name = 'consultorio'

urlpatterns = [
    path('list/', ListAreaSalud.as_view(), name='ListAreaSalud'),
    path('add/', AddAreaSalud.as_view(), name='AddAreaSalud'),
    path('update/<int:pk>', UpdateAreaSalud.as_view(), name='UpdateAreaSalud'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
