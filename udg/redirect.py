from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def redirectLogin(request):
    return redirect('login:Login')