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


# Format (А2 - А6 и т.д.)
class Format(models.Model):
    format = models.CharField(max_length=20)

    def __str__(self):
        return self.format


# Orientation (ориентация горизонтальная или вертикальная)
class Orientation(models.Model):
    orientation = models.CharField(max_length=14)

    def __str__(self):
        return self.orientation


# Shop number (номер магазина)
class Shop(models.Model):
    shop = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.shop)


# Warehouse (место хранения, название склада)
class Warehouse(models.Model):
    warehouse = models.CharField(max_length=30)

    def __str__(self):
        return self.warehouse


#########################
# Pockets class section #
#########################

# Pocket additional pockets (дополнительные карманы и их размеры)
class PocketOption(models.Model):
    pockets = models.CharField(max_length=10, blank=True)
    size = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return '{} {}'.format(self.pockets, self.size)


# Pocket type (подвесной, клейкий, магнитный и т.д.)
class PocketType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


# Pocket Main Model (описание основной модели карманов)
class Pocket(models.Model):
    type = models.ForeignKey(PocketType, on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    format = models.ForeignKey(Format, on_delete=models.SET_NULL, null=True, verbose_name='Формат')
    orientation = models.ForeignKey(Orientation, on_delete=models.SET_NULL, null=True, verbose_name='Ориентация')
    option = models.ForeignKey(PocketOption, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Дополнительные опции')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, verbose_name='Склад')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Адрес на складе')
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, verbose_name='Магазин')
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
