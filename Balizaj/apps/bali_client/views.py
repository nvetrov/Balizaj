from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import *


# Create your views here.
from .models import Pocket


def index(request):
    return render(request, 'client/index.html', {})


def pockets_type(request):
    template = loader.get_template('client/pockets_type.html')
    type_data = {'type_data': PocketType.objects.all()}
    return HttpResponse(template.render(type_data, request))


def priceholders_type(request):
    template = loader.get_template('client/priceholders_type.html')
    type_data = {'type_data': PriceHolderType.objects.all()}
    return HttpResponse(template.render(type_data, request))


def plasticholders_type(request):
    template = loader.get_template('client/plasticholders_type.html')
    type_data = {'type_data': PlasticHolderType.objects.all()}
    return HttpResponse(template.render(type_data, request))


def pricepaper_type(request):
    template = loader.get_template('client/pricepaper_type.html')
    type_data = {'type_data': PricePaperType.objects.all()}
    return HttpResponse(template.render(type_data, request))


def other_type(request):
    template = loader.get_template('client/other_type.html')
    type_data = {'type_data': OtherType.objects.all()}
    return HttpResponse(template.render(type_data, request))


def pockets(request, name, type_id):
    dict = {'pockets': [Pocket.objects.filter(type=type_id), 'Карманы'],
            'priceholders': [PriceHolder.objects.filter(type=type_id), 'Ценникодержатели'],
            'plastikholders': [PlasticHolder.objects.filter(type=type_id), 'Пластиковые держатели'],
            'pricepaper': [PricePaper.objects.filter(type=type_id), 'Бумага'],
            'others': [Other.objects.filter(type=type_id), 'Прочее']
            }
    template = loader.get_template('client/materials.html')
    type_data = {'materials': dict[name][0], 'material_name': dict[name][1]}
    return HttpResponse(template.render(type_data, request))
