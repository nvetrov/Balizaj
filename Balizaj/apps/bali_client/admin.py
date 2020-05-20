from django.contrib import admin
from .models import *


# Register your models here.
#######################
# Shared Options Admin#
#######################
@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
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
@admin.register(PriceHolder)
class PriceHolderInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


#####################
# Price Paper Admin #
#####################
@admin.register(PricePaper)
class PricePaperInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


######################
# Price Holder Admin #
######################
@admin.register(PlasticHolder)
class PlasticHolderInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')


######################
# Price Holder Admin #
######################

@admin.register(Other)
class OtherInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')
