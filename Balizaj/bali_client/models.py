# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

#######################################
# Shared options  (общее для моделей) #
#######################################

# Address in warehouse (адрес на складе (если есть))
class Address(models.Model):
    address = models.CharField(max_length=10)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Складской адрес'
        verbose_name_plural = 'Складские адреса'


# Format (А2 - А6 и т.д.)
class Format(models.Model):
    format = models.CharField(max_length=20)

    def __str__(self):
        return self.format

    class Meta:
        verbose_name = 'Формат бумаги (включая нестандартные)'
        verbose_name_plural = 'Форматы бумаги (включая нестандартные)'


# Additional options (дополнительные карманы и их размеры, прочие опции)
class Option(models.Model):
    option = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.option

    class Meta:
        verbose_name = 'Дополнительные опции (доп. карманы, размеры доп. карманов, габариты)'
        verbose_name_plural = 'Дополнительная опция (карман, размер и т.д.)'


# Orientation (ориентация горизонтальная или вертикальная)
class Orientation(models.Model):
    orientation = models.CharField(max_length=14)

    def __str__(self):
        return self.orientation

    class Meta:
        verbose_name = 'Ориентация бумаги'
        verbose_name_plural = 'Ориентации бумаги'


# Type (подвесной, клейкий, магнитный и т.д.)
class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


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

    def __str__(self):
        return self.warehouse

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class SharedOption(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, verbose_name='Склад')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Адрес на складе')
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, verbose_name='Магазин')


#########################
# Pockets class section #
#########################

# Pocket Main Model (описание основной модели карманов)
class Pocket(SharedOption):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(Format, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    orientation = models.ForeignKey(Orientation, on_delete=models.SET_NULL, null=True, verbose_name='Ориентация')
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Дополнительные опции')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='images/pockets', blank=True, verbose_name='Изображение')

    def __str__(self):
        if self.option == None:
            return '{} {} {}, находится - {}, количество - {}'.format(self.type,
                                                                      self.format,
                                                                      self.orientation,
                                                                      self.warehouse,
                                                                      self.quantity
                                                                      )
        else:
            return '{} {} {} {}, находится - {}, количество - {}'.format(self.type,
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
    priceholderformat = models.CharField(max_length=15)

    def __str__(self):
        return self.priceholderformat

    class Meta:
        verbose_name = 'Формат ценникодержателя'
        verbose_name_plural = 'Форматы ценникодержателей (DBR20, DBR60 и т.д.)'


# Price Holder Main Model (описание основной модели ценникодержателей)
class PriceHolder(SharedOption):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(PriceHolderFormat, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, verbose_name='Дополнительные опции')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='images/priceholders', blank=True, verbose_name='Изображение')

    def __str__(self):
        if self.option == None:
            return '{} {}, находится - {}, количество - {}'.format(self.type,
                                                                   self.format,
                                                                   self.warehouse,
                                                                   self.quantity
                                                                   )
        else:
            return '{} {} {}, находится - {}, количество - {}'.format(self.type,
                                                                      self.format,
                                                                      self.option,
                                                                      self.warehouse,
                                                                      self.quantity
                                                                      )

    class Meta:
        verbose_name = 'Ценникодержатель'
        verbose_name_plural = 'Ценникодержатели'


############################
# PricePaper class section #
############################


# Paper type (Фейсинги, Оффсеты и т.д.)
class PricePaperType(models.Model):
    papertype = models.CharField(max_length=20)

    def __str__(self):
        return self.papertype

    class Meta:
        verbose_name = 'Тип бумаги для ценников'
        verbose_name_plural = 'Типы бумаги для ценников'


# Price Paper Main Model (описание основной модели)
class PricePaper(SharedOption):
    type = models.ForeignKey(PricePaperType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(Format, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='images/pricepapers', blank=True, verbose_name='Изображение')

    def __str__(self):
        return '{} {}, находится - {}, количество - {}'.format(self.type,
                                                               self.format,
                                                               self.warehouse,
                                                               self.quantity
                                                               )

    class Meta:
        verbose_name = 'Бумага для ценников'
        verbose_name_plural = 'Бумага для ценников'


###############################
# PlasticHolder class section #
###############################

# Plastic holder type (виды держателей)
class PlasticHolderType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип пластикового держателя'
        verbose_name_plural = 'Типы пластиковых держателей'


# Plastic holder position (настенный, настольный, наполный)
class PlasticHolderPosition(models.Model):
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Тип размещения пластикового держателя'
        verbose_name_plural = 'Типы размещений пластиковых держателей'


# Plastic Holder Main Model
class PlasticHolder(SharedOption):
    type = models.ForeignKey(PlasticHolderType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    orientation = models.ForeignKey(Orientation, on_delete=models.SET_NULL, null=True, verbose_name='Ориентация')
    position = models.ForeignKey(PlasticHolderPosition, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Размещение')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='images/plasticholders', blank=True, verbose_name='Изображение')

    def __str__(self):
        return '{} {} {}, находится - {}, количество - {}'.format(self.type,
                                                                  self.orientation,
                                                                  self.position,
                                                                  self.warehouse,
                                                                  self.quantity
                                                                  )

    class Meta:
        verbose_name = 'Пластиковый держатель'
        verbose_name_plural = 'Пластиковые держатели'


#######################
# Other class section #
#######################

# Other type (виды разных держателей и т.д.)
class OtherType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Прочее - тип'
        verbose_name_plural = 'Прочее - типы'


# Other name (наименование)
class OtherName(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прочее - полное наименование'
        verbose_name_plural = 'Прочее - полные наименования'


# Other Main Model (основная модель)
class Other(SharedOption):
    type = models.ForeignKey(OtherType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    name = models.ForeignKey(OtherName, on_delete=models.SET_NULL, null=True, verbose_name='Наименование')
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='images/others', blank=True, verbose_name='Изображение')

    def __str__(self):
        return '{} {}, находится - {}, количество - {}'.format(self.type,
                                                               self.name,
                                                               self.warehouse,
                                                               self.quantity
                                                               )

    class Meta:
        verbose_name = 'Прочее'
        verbose_name_plural = 'Прочее'
