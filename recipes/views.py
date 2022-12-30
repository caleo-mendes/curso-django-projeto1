from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse('Home')


def contact(request):
    return HttpResponse('Contato')


def about(request):
    return HttpResponse('Sobre')
