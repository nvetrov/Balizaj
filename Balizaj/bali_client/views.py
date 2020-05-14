from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def pockets(request):
    return render(request, 'pockets.html', {})


def priceholders(request):
    return render(request, 'priceholders.html', {})


def plasticholders(request):
    return render(request, 'plasticholders.html', {})


def pricepaper(request):
    return render(request, 'pricepaper.html', {})


def other(request):
    return render(request, 'other.html', {})