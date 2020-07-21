from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.contrib import auth
from Balizaj.apps.bali_client.mag_number_auth import Auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Страница авторизации
def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_user = (request.POST['login'])
            password = (request.POST['password'])
            user_auth = Auth(login_user, password)
            if user_auth.user_valid():
                user = auth.authenticate(username=login_user, password=password)
                if user is not None:
                    user = User.objects.get(username=user_auth.login)
                    user.set_password(user_auth.password)
                    user.save()
                    login(request, user)
                else:
                    user = User.objects.create_user(username=user_auth.login)
                    user.set_password(user_auth.password)
                    profile = UserProfile.objects.create(shop_verbose=user_auth.shop_verbose,
                                                         shop_number=user_auth.shop_number,
                                                         group=user_auth.group,
                                                         user=user)
                    user.save()
                    profile.save()
                    login(request, user)
                profile = UserProfile.objects.get(user=user)
                data = {'profile': profile}
                if profile.group == 'client':
                    template = loader.get_template('client/index.html')
                    return HttpResponse(template.render(data, request))

                elif profile.group == 'bali':
                    template = loader.get_template('bali/index.html')
                    return HttpResponse(template.render(data, request))
        return render(request, 'index.html')

    if request.user.is_authenticated:
        print('authorised')
        profile = UserProfile.objects.get(user=request.user)
        data = {'profile': profile}
        if profile.group == 'client':
            print('client')
            template = loader.get_template('client/index.html')
            return HttpResponse(template.render(data, request))

        elif profile.group == 'bali':
            print('bali')
            template = loader.get_template('bali/index.html')
            return HttpResponse(template.render(data, request))
    return render(request, 'client/index.html', {})


# Страница выбора типа материалов
@login_required(login_url='/')
def client_index(request):
    print(request.user)
    return render(request, 'client/index.html', {})


# Страница выбора типа карманов
@login_required(login_url='/')
def pockets_type(request):
    template = loader.get_template('client/pockets_type.html')
    profile = UserProfile.objects.get(user=request.user)
    type_data = {'type_data': PocketType.objects.all(),
                 'profile': profile}
    return HttpResponse(template.render(type_data, request))


# Страница выбора типа ценникодержателей
@login_required(login_url='/')
def priceholders_type(request):
    profile = UserProfile.objects.get(user=request.user)
    template = loader.get_template('client/priceholders_type.html')
    type_data = {'type_data': PriceHolderType.objects.all(),
                 'profile': profile}
    return HttpResponse(template.render(type_data, request))


# Страница выбора типа плстаиковых держателей
@login_required(login_url='/')
def plasticholders_type(request):
    profile = UserProfile.objects.get(user=request.user)
    template = loader.get_template('client/plasticholders_type.html')
    type_data = {'type_data': PlasticHolderType.objects.all(),
                 'profile': profile}
    return HttpResponse(template.render(type_data, request))


# Страница выбора типа бумаги для ценников
@login_required(login_url='/')
def pricepaper_type(request):
    profile = UserProfile.objects.get(user=request.user)
    template = loader.get_template('client/pricepaper_type.html')
    type_data = {'type_data': PricePaperType.objects.all(),
                 'profile': profile}
    return HttpResponse(template.render(type_data, request))


# Страница выбора типа прочих материалов
@login_required(login_url='/')
def other_type(request):
    profile = UserProfile.objects.get(user=request.user)
    template = loader.get_template('client/other_type.html')
    type_data = {'type_data': OtherType.objects.all(),
                 'profile': profile}
    return HttpResponse(template.render(type_data, request))


# Страница генерации материалов после выбора типа (общая для всех материалов)
@login_required(login_url='/')
def materials(request, name, type_id):
    profile = UserProfile.objects.get(user=request.user)
    shop = (str(profile.shop_number))
    materials_dict = {'pockets': [Pocket.objects.filter(type=type_id).filter(shop__in=shop).order_by('-orientation', '-format'), 'Карманы'],
                      'priceholders': [PriceHolder.objects.filter(type=type_id).filter(shop__in=shop), 'Ценникодержатели'],
                      'plasticholders': [PlasticHolder.objects.filter(type=type_id).filter(shop__in=shop), 'Пластиковые держатели'],
                      'pricepapers': [PricePaper.objects.filter(type=type_id).filter(shop__in=shop), 'Бумага'],
                      'others': [Other.objects.filter(type=type_id).filter(shop__in=shop), 'Прочее']
                      }
    template = loader.get_template('client/materials.html')
    type_data = {'materials': materials_dict[name][0],
                 'material_name': materials_dict[name][1],
                 'profile': profile}

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

    return HttpResponse(template.render(type_data, request))


# Внутренняя функция, возвращает словарь из всех материалов с непустым значением "cart_count"
# (значит материал есть в корзине)
def material_dict():
    pockets = Pocket.objects.exclude(cart_count=0).order_by('-type', '-format', '-orientation')
    pricholders = PriceHolder.objects.exclude(cart_count=0)
    plasticholders = PlasticHolder.objects.exclude(cart_count=0)
    pricepaper = PricePaper.objects.exclude(cart_count=0)
    other = Other.objects.exclude(cart_count=0)
    data = {'pockets': pockets,
            'priceholders': pricholders,
            'plasticholders': plasticholders,
            'pricepapers': pricepaper,
            'others': other}
    return data


# Страница генерации корзины, для генерации использует material_dict()
@login_required(login_url='/')
def cart(request):
    profile = UserProfile.objects.get(user=request.user)
    template = loader.get_template('client/cart.html')

    if request.method == 'POST':
        print(request.POST)
        material = material_dict()[request.POST['name']].get(id=int(request.POST['id']))
        material.cart_count = 0
        material.cart_quantity = 0
        material.save()
    cart_materials = material_dict()
    cart_materials['profile'] = profile
    return HttpResponse(template.render(cart_materials, request))


# Выбор отдела списания
@login_required(login_url='/')
def choose_department(request):
    template = loader.get_template('client/choose_department.html')
    department = Department.objects.all()
    data = {'profile': UserProfile.objects.get(user=request.user), 'department': department}
    if request.method == 'POST':
        if request.POST['department'] == '--':
            return HttpResponse(template.render(data, request))
        else:
            template = loader.get_template('client/index.html')
            write_off(request.POST['department'], data['profile'].shop_number)
            return HttpResponse(template.render(data, request))
    return HttpResponse(template.render(data, request))


# Внутренняя функция корзины, списывает все материалы которые остались в корзине и записывает их в списанные.
def write_off(department, shop_number):
    for materials_write_off in material_dict().values():
        for material in materials_write_off:
            a = WriteOffMaterial()
            a.type = material.material_type
            a.name = material
            a.quantity = material.cart_count
            a.shop = shop_number
            a.department = department
            a.save()
            print(a.date)
            print(a.time)
            print(a.shop)
            material.quantity -= material.cart_count
            material.cart_count = 0
            material.cart_quantity = 0
            material.save()
