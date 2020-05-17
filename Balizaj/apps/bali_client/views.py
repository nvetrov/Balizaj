from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def pockets(request, type = 0):
    template = loader.get_template('pockets.html')
    pockets_type = {'pockets_type': Type.objects.filter(Pocket)}
    pockets_data = {'pockets': Pocket.objects.all()}
    return HttpResponse(template.render(pockets_data, pockets_type, request))


def priceholders(request):
    return render(request, 'priceholders.html', {})


def plasticholders(request):
    return render(request, 'plasticholders.html', {})


def pricepaper(request):
    return render(request, 'pricepaper.html', {})


def other(request):
    return render(request, 'other.html', {})