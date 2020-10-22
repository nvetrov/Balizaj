from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Balizaj.apps.bali_client.models import *
import datetime
from django.db.models import Sum


# получение текущего пользователя
def current_user(request):
    profile = UserProfile.objects.get(user=request.user)
    current_date = datetime.date.today()
    shop_id = Shop.objects.get(shop=profile.shop_number)

    data = {'profile': profile,
            'shop': profile.shop_number,
            'department': Department.objects.all(),
            'current_date': current_date.strftime('%Y-%m-%d'),
            'shop_id': shop_id
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


def warehouse_material(shop_id, warehouse):
    pockets = Pocket.objects.filter(shop=shop_id).filter(warehouse=warehouse,
                                                         quantity__gt=0)
    priceholders = PriceHolder.objects.filter(shop=shop_id).filter(warehouse=warehouse,
                                                                   quantity__gt=0)
    plasticholders = PlasticHolder.objects.filter(shop=shop_id).filter(warehouse=warehouse,
                                                                       quantity__gt=0)
    pricepaper = PricePaper.objects.filter(shop=shop_id).filter(warehouse=warehouse,
                                                                quantity__gt=0)
    other = Other.objects.filter(shop=shop_id).filter(warehouse=warehouse,
                                                      quantity__gt=0)
    data = {'pockets': pockets,
            'priceholders': priceholders,
            'plasticholders': plasticholders,
            'pricepapers': pricepaper,
            'others': other}
    return data


# Страница перемещения между складами
@login_required(login_url='/')
def select_move_storage(request):
    print(request)
    template = loader.get_template('bali/index_storages.html')
    user = current_user(request)
    data = {**user}
    ware_start = Warehouse.objects\
        .filter(sharedoption__shop__shop=Shop.objects.get(shop=data['shop']).shop)\
        .order_by('warehouse')\
        .distinct()
    data['ware_start'] = ware_start
    if request.method == 'POST':
        template = loader.get_template('bali/storage_materials.html')
        ware_id = Warehouse.objects.get(warehouse=request.POST['warehouse-start'])
        warehouse_selected = Warehouse.objects.get(warehouse=ware_id)
        ware_end = Warehouse.objects.filter(shop=data['shop_id'])\
            .order_by('warehouse')\
            .exclude(warehouse=warehouse_selected)
        data = {
            **user,
            **warehouse_material(user['shop_id'], ware_id.id),
            'ware_end': ware_end,
            'warehouse_selected': warehouse_selected
        }
        return HttpResponse(template.render(data, request))
    return HttpResponse(template.render(data, request))


def move_materials(request):
    print(request.POST)
    return request

