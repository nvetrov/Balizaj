from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.contrib import auth
from Balizaj.apps.bali_client.mag_number_auth import Auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from Balizaj.apps.bali_client.models import UserProfile, WriteOffMaterial, Department
import datetime
from django.db.models import Sum

# получение текущего пользователя
def current_user(request):
    profile = UserProfile.objects.get(user=request.user)
    current_date = datetime.date.today()

    data = {'profile': profile,
            'shop': profile.shop_number,
            'department': Department.objects.all(),
            'current_date': current_date.strftime('%Y-%m-%d')
            }
    return data


# страница формирования отчётов
@login_required(login_url='/')
def reports(request):
    template = loader.get_template('bali/shop-report.html')
    data = current_user(request)
    if request.method == 'POST':
        template = loader.get_template('bali/report.html')
        data['start'] = request.POST['start-date']
        data['end'] = request.POST['end-date']
        start = datetime.datetime.strptime(request.POST['start-date'], '%Y-%m-%d').date()
        end = datetime.datetime.strptime(request.POST['end-date'], '%Y-%m-%d').date()
        data['department'] = request.POST['department']
        if request.POST['department'] == 'Общий':
            materials = WriteOffMaterial.objects \
                .filter(shop=data['shop']) \
                .filter(date__range=(start, end)) \
                .values('type', 'name') \
                .annotate(summa=Sum('quantity')).order_by('type')
        else:
            materials = WriteOffMaterial.objects \
                .filter(shop=data['shop']) \
                .filter(department=request.POST['department']) \
                .filter(date__range=(start, end)) \
                .values('type', 'name') \
                .annotate(summa=Sum('quantity')).order_by('type')
        pockets = materials.filter(type='Карман')
        data['pockets'] = pockets
        pricepapers = materials.filter(type='Бумага для ценников')
        data['pricepapers'] = pricepapers
        plasticholders = materials.filter(type='Пластиковый держатель')
        data['plasticholders'] = plasticholders
        priceholders = materials.filter(type='Ценникодержатель')
        data['priceholders'] = priceholders
        others = materials.filter(type='Прочее')
        data['others'] = others
        return HttpResponse(template.render(data, request))
    return HttpResponse(template.render(data, request))
