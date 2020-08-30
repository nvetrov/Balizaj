# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


##########################################################################################
#                                   User Profile Model                                   #
##########################################################################################


class UserProfile(models.Model):
    shop_number = models.SmallIntegerField(verbose_name='Номер магазина')
    shop_verbose = models.CharField(max_length=50, verbose_name='Название магазина')
    group = models.CharField(max_length=10, null=True, verbose_name='Группа пользователя')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='LDAP')

    def __str__(self):
        return self.shop_verbose

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


#########################################################################################
#                          Material models (модели материалов)                          #
#########################################################################################

##################################################
# Shared options  (общее для моделей материалов) #
##################################################

# Address in warehouse (адрес на складе (если есть))
class Address(models.Model):
    address = models.CharField(max_length=10)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Складской адрес'
        verbose_name_plural = 'Складские адреса'


# Shop number (номер магазина)
class Shop(models.Model):
    shop = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.shop)

    class Meta:
        verbose_name = 'Номер магазина'
        verbose_name_plural = 'Номера магазинов'


# Warehouse (место хранения, название склада)
class Warehouse(models.Model):
    warehouse = models.CharField(max_length=30)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, verbose_name='Магазин')

    def __str__(self):
        return self.warehouse

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


# Shared Option Main Model (Опции общие для всех материалов)
class SharedOption(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, verbose_name='Склад')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Адрес на складе')
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, verbose_name='Магазин')


#########################
# Pockets class section #
#########################

# PocketFormat (А2 - А6 и т.д.)
class PocketFormat(models.Model):
    format = models.CharField(max_length=20)

    def __str__(self):
        return self.format

    class Meta:
        verbose_name = 'Формат кармана'
        verbose_name_plural = 'Форматы карманов'


# Additional options (дополнительные карманы и их размеры, прочие опции)
class PocketOption(models.Model):
    option = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.option

    class Meta:
        verbose_name = 'Дополнительные опции (доп. карманы, размеры доп. карманов, габариты)'
        verbose_name_plural = 'Дополнительная опция (карман, размер и т.д.)'


# Orientation (ориентация горизонтальная или вертикальная)
class PocketOrientation(models.Model):
    orientation = models.CharField(max_length=14)

    def __str__(self):
        return self.orientation

    class Meta:
        verbose_name = 'Ориентация кармана'
        verbose_name_plural = 'Ориентация карманов'


# PocketType (подвесной, клейкий, магнитный и т.д.)
class PocketType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


# Pocket Main Model (описание основной модели карманов)
class Pocket(SharedOption):
    material_type = models.CharField(max_length=6, default='Карман', verbose_name='Карман')
    type = models.ForeignKey(PocketType, on_delete=models.SET_NULL, null=True, verbose_name='Тип кармана')
    format = models.ForeignKey(PocketFormat, on_delete=models.SET_NULL, null=True, verbose_name='Формат кармана')
    orientation = models.ForeignKey(PocketOrientation, on_delete=models.SET_NULL, null=True,
                                    verbose_name='Ориентация кармана')
    option = models.ForeignKey(PocketOption, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Дополнительные опции')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    cart_quantity = models.SmallIntegerField(default=0, verbose_name='Доступно для списания')
    cart_count = models.SmallIntegerField(default=0, verbose_name='В корзине')
    image = models.ImageField(upload_to='images/pockets', blank=True, verbose_name='Изображение')

    def getImage(self):
        if not self.image:
            return 'images/Default.png'
        else:
            return self.image

    def __str__(self):
        if self.option is None:
            return '{} {} {}'.format(self.type,
                                     self.format,
                                     self.orientation
                                     )
        else:
            return '{} {} {} {}'.format(self.type,
                                        self.format,
                                        self.orientation,
                                        self.option,
                                        self.warehouse,
                                        self.quantity
                                        )

    class Meta:
        verbose_name = 'Карман'
        verbose_name_plural = 'Карманы'


#############################
# PriceHolder class section #
#############################

# Price holder format (DBR20, DBR60, KE39 и т.д.)
class PriceHolderFormat(models.Model):
    format = models.CharField(max_length=15)

    def __str__(self):
        return self.format

    class Meta:
        verbose_name = 'Формат ценникодержателя (DBR20, DBR60 и т.д.)'
        verbose_name_plural = 'Форматы ценникодержателей (DBR20, DBR60 и т.д.)'


# Price holder height (высота ценникодержателя)
class PriceHolderHeight(models.Model):
    height = models.CharField(max_length=10, verbose_name='Высота')

    def __str__(self):
        return self.height

    class Meta:
        verbose_name = 'Высота ценникодержателя'
        verbose_name_plural = 'Высота ценникодержателей'


# Price holder type (тип ценникодержателя подвесной, клейкий, магнитный и т.д.)
class PriceHolderType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип ценникодержателя'
        verbose_name_plural = 'Типы ценникодержателя'


# Price holder wight (ширина ценникодержателя)
class PriceHolderWight(models.Model):
    widht = models.CharField(max_length=10, verbose_name='Ширина')

    def __str__(self):
        return self.widht

    class Meta:
        verbose_name = 'Ширина ценникодержателя'
        verbose_name_plural = 'Ширина ценникодержателей'


# Price Holder Main Model (описание основной модели ценникодержателей)
class PriceHolder(SharedOption):
    material_type = models.CharField(max_length=16, default='Ценникодержатель', verbose_name='Ценникодержатель')
    type = models.ForeignKey(PriceHolderType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(PriceHolderFormat, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    height = models.ForeignKey(PriceHolderHeight, on_delete=models.SET_NULL, null=True, verbose_name='Высота')
    wight = models.ForeignKey(PriceHolderWight, on_delete=models.SET_NULL, null=True, verbose_name='Ширина')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    cart_quantity = models.SmallIntegerField(default=0, verbose_name='Доступно для списания')
    cart_count = models.SmallIntegerField(default=0, verbose_name='В корзине')
    image = models.ImageField(upload_to='images/priceholders', blank=True, verbose_name='Изображение')

    def getImage(self):
        if not self.image:
            return 'images/Default.jpg'
        else:
            return self.image

    def __str__(self):
        if self.wight and self.height is None:
            return '{} {}'.format(self.type,
                                  self.format,
                                  )
        else:
            return '{} {} высота {} ширина {}'.format(self.type,
                                                      self.format,
                                                      self.height,
                                                      self.wight,
                                                      self.warehouse,
                                                      self.quantity
                                                      )

    class Meta:
        verbose_name = 'Ценникодержатель'
        verbose_name_plural = 'Ценникодержатели'


############################
# PricePaper class section #
############################

# Price paper format (формат бумаги для ценников)
class PricePaperFormat(models.Model):
    format = models.CharField(max_length=15)

    def __str__(self):
        return self.format

    class Meta:
        verbose_name = 'Формат бумаги для ценников (А2, А3 и т.д.)'
        verbose_name_plural = 'Форматы бумаги для ценников (А2, А3 и т.д.)'


# Paper type (Фейсинги, Оффсеты и т.д.)
class PricePaperType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип бумаги для ценников'
        verbose_name_plural = 'Типы бумаги для ценников'


# Price Paper Main Model (описание основной модели)
class PricePaper(SharedOption):
    material_type = models.CharField(max_length=19, default='Бумага для ценников', verbose_name='Бумага для ценников')
    type = models.ForeignKey(PricePaperType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(PricePaperFormat, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    cart_quantity = models.SmallIntegerField(default=0, verbose_name='Доступно для списания')
    cart_count = models.SmallIntegerField(default=0, verbose_name='В корзине')
    image = models.ImageField(upload_to='images/pricepapers', blank=True, verbose_name='Изображение')

    def getImage(self):
        if not self.image:
            return 'images/Default.jpg'
        else:
            return self.image

    def __str__(self):
        return '{} {}'.format(self.type,
                              self.format,
                              )

    class Meta:
        verbose_name = 'Бумага для ценников'
        verbose_name_plural = 'Бумага для ценников'


###############################
# PlasticHolder class section #
###############################

# Plastic holder format (формат (А2, А3 и т.д.))
class PlasticHolderFormat(models.Model):
    format = models.CharField(max_length=10, verbose_name='Формат')

    def __str__(self):
        return self.format

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'


# Plastic holder orientation (ориентация горизонтальная или вертикальная)
class PlasticHolderOrientation(models.Model):
    orientation = models.CharField(max_length=14, verbose_name='Ориентация')

    def __str__(self):
        return self.orientation

    class Meta:
        verbose_name = 'Ориентация пластикового держателя'
        verbose_name_plural = 'Ориентация пластиковых держателей'


# Plastic holder position (настенный, настольный)
class PlasticHolderPosition(models.Model):
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Тип размещения пластикового держателя'
        verbose_name_plural = 'Типы размещения пластикового держателя'


# Plastic holder type (виды держателей)
class PlasticHolderType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип пластикового держателя'
        verbose_name_plural = 'Типы пластиковых держателей'


# Plastic Holder Main Model
class PlasticHolder(SharedOption):
    material_type = models.CharField(max_length=21, default='Пластиковый держатель',
                                     verbose_name='Пластиковый держатель')
    type = models.ForeignKey(PlasticHolderType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(PlasticHolderFormat, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    orientation = models.ForeignKey(PlasticHolderOrientation, on_delete=models.SET_NULL, null=True,
                                    verbose_name='Ориентация')
    position = models.ForeignKey(PlasticHolderPosition, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Размещение')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    cart_quantity = models.SmallIntegerField(default=0, verbose_name='Доступно для списания')
    cart_count = models.SmallIntegerField(default=0, verbose_name='В корзине')
    image = models.ImageField(upload_to='images/plasticholders', blank=True, verbose_name='Изображение')

    def getImage(self):
        if not self.image:
            return 'images/Default.jpg'
        else:
            return self.image

    def __str__(self):
        if self.position is None:
            return '{} {} {}'.format(self.type,
                                     self.format,
                                     self.orientation,
                                     )
        else:
            return '{} {} {} {}'.format(self.type,
                                        self.format,
                                        self.orientation,
                                        self.position,
                                        )

    class Meta:
        verbose_name = 'Пластиковый держатель'
        verbose_name_plural = 'Пластиковые держатели'


#######################
# Other class section #
#######################
# Other name (наименование)
class OtherName(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прочее - полное наименование'
        verbose_name_plural = 'Прочее - полные наименования'


# Other type (виды разных держателей и т.д.)
class OtherType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Прочее - тип (держатели, для стрелок, для профиля и т.д.)'
        verbose_name_plural = 'Прочее - типы (держатели, для стрелок, для профиля и т.д.)'


# Other Main Model (основная модель)
class Other(SharedOption):
    material_type = models.CharField(max_length=6, default='Прочее', verbose_name='Прочее')
    type = models.ForeignKey(OtherType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    name = models.ForeignKey(OtherName, on_delete=models.SET_NULL, null=True, verbose_name='Наименование')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    cart_quantity = models.SmallIntegerField(default=0, verbose_name='Доступно для списания')
    cart_count = models.SmallIntegerField(default=0, verbose_name='В корзине')
    image = models.ImageField(upload_to='images/others', blank=True, verbose_name='Изображение')

    def getImage(self):
        if not self.image:
            return 'images/Default.jpg'
        else:
            return self.image

    def __str__(self):
        return '{} {}'.format(self.type,
                              self.name,
                              )

    class Meta:
        verbose_name = 'Прочее'
        verbose_name_plural = 'Прочее'


##########################################################################################
#                                   Write Off Material                                   #
##########################################################################################

class WriteOffMaterial(models.Model):
    type = models.CharField(max_length=40, verbose_name='Тип материала')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    name = models.CharField(max_length=80, verbose_name='Полное наименование материала')
    date = models.DateField(auto_now_add=True, verbose_name='Дата списания')
    time = models.TimeField(auto_now_add=True, verbose_name='Время списания')
    department = models.CharField(max_length=10, default='Общий', verbose_name='Номер отдела')
    shop = models.CharField(max_length=5, default='000', verbose_name='Номер магазина')

    def __str__(self):
        return '{} {}'.format(self.type, self.name)

    class Meta:
        verbose_name = 'Списанный материал'
        verbose_name_plural = 'Списанные материалы'


#################
#   Department  #
#################

class Department(models.Model):
    department = models.CharField(max_length=20, verbose_name='Номер отдела')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = 'Номер отдела'
        verbose_name_plural = 'Номера отделов'
