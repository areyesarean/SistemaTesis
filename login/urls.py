from django.urls import path

from login.views import LoginTView, CerrarSession, ChangePassword, UdateUSerView

app_name = 'login'

urlpatterns = [
    path('', LoginTView.as_view(), name='Login'),
    path('logout/', CerrarSession.as_view(), name='Logout'),
    path('changePassword/', ChangePassword.as_view(), name='ChangePassword'),
    path('updateUser/', UdateUSerView.as_view(), name='UdateUSerView'),
]
