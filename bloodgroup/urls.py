from django.urls import path

from bloodgroup.views import ListBloodGroup, AddBloodGroup, UpdateBloodGroup

app_name = 'bloodgroup'

urlpatterns = [
    path('list/', ListBloodGroup.as_view(), name='ListBloodGroup'),
    path('add/', AddBloodGroup.as_view(), name='AddBloodGroup'),
    path('update/<int:pk>', UpdateBloodGroup.as_view(), name='UpdateBloodGroup'),
    # path('delete/<int:pk>', DeleteEstudiante.as_view(), name='DeleteEstudiante'),
    # path('pdf/', PdfEstudiantesView.as_view(), name='PdfEstudiantesView'),
]
