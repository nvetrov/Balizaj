from django.contrib import admin
from .models import *


# Register your models here.
#######################
# Shared Options Admin#
#######################

@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Format)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Orientation)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class AuthorAdmin(admin.ModelAdmin):
    pass


################
# Pocket Admin #
################

@admin.register(Pocket)
class PocketInstanseAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


######################
# Price Holder Admin #
######################

@admin.register(PriceHolderFormat)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceHolder)
class PriceHolderInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


#####################
# Price Paper Admin #
#####################

@admin.register(PricePaperType)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PricePaper)
class PricePaperInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


######################
# Price Holder Admin #
######################

@admin.register(PlasticHolderType)
class PriceHolderAdmin(admin.ModelAdmin):
    pass


@admin.register(PlasticHolderPosition)
class PlasticHolderPosition(admin.ModelAdmin):
    pass


@admin.register(PlasticHolder)
class PlasticHolderInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


######################
# Price Holder Admin #
######################

@admin.register(OtherType)
class OtherTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(OtherName)
class OtherNamePosition(admin.ModelAdmin):
    pass


@admin.register(Other)
class OtherInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')
