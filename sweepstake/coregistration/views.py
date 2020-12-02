from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def coreg(request):
    return render(request, 'coregistration/coregistration.html')