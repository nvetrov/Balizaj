from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

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


def materials(request, name, type_id):
    materials_dict = {'pockets': [Pocket.objects.filter(type=type_id), 'Карманы'],
                      'priceholders': [PriceHolder.objects.filter(type=type_id), 'Ценникодержатели'],
                      'plastikholders': [PlasticHolder.objects.filter(type=type_id), 'Пластиковые держатели'],
                      'pricepaper': [PricePaper.objects.filter(type=type_id), 'Бумага'],
                      'others': [Other.objects.filter(type=type_id), 'Прочее']
                      }
    template = loader.get_template('client/materials.html')
    type_data = {'materials': materials_dict[name][0], 'material_name': materials_dict[name][1]}
    if request.method == 'POST':
        if request.POST['to_cart'] == '':
            return HttpResponse(template.render(type_data, request))
        cart_object = materials_dict[name][0].get(id=request.POST['type'])
        counter = int(request.POST['to_cart'])
        if (cart_object.cart_quantity - counter) <= 0:
            cart_object.cart_count += cart_object.cart_quantity
            cart_object.cart_quantity = 0
        else:
            cart_object.cart_quantity -= int(request.POST['to_cart'])
            cart_object.cart_count += int(request.POST['to_cart'])
        cart_object.save()
        return HttpResponse(template.render(type_data, request))
    for item in materials_dict[name][0]:
        if item.cart_quantity == 0:
            item.cart_quantity = item.quantity
            item.save()
        print(item.cart_quantity)
    return HttpResponse(template.render(type_data, request))


def material_dict():
    pockets = Pocket.objects.exclude(cart_count=0).order_by('type', '-format', '-orientation')
    pricholders = PriceHolder.objects.exclude(cart_count=0)
    plasticholders = PlasticHolder.objects.exclude(cart_count=0)
    pricepaper = PricePaper.objects.exclude(cart_count=0)
    other = Other.objects.exclude(cart_count=0)
    data = {'pockets': pockets,
            'priceholders': pricholders,
            'plasticholders': plasticholders,
            'pricepaper': pricepaper,
            'other': other}
    return data


def cart(request):
    template = loader.get_template('client/cart.html')

    if request.method == 'POST':
        material = material_dict()[request.POST['name']].get(id=int(request.POST['id']))
        material.cart_count = 0
        material.cart_quantity = 0
        material.save()
        material_dict()
    return HttpResponse(template.render(material_dict(), request))


def write_off(request):
    for materials_write_off in material_dict().values():
        for material in materials_write_off:
            material.quantity -= material.cart_count
            material.cart_count = 0
            material.cart_quantity = 0
            material.save()
    return render(request, 'client/index.html', {})
