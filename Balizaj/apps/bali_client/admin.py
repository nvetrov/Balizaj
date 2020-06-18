from django.contrib import admin
from .models import *

################
# User Profile #
################

@admin.register(UserProfile)
class AuthorAdmin(admin.ModelAdmin):
    pass


#######################
# Shared Options Admin#
#######################
@admin.register(Address, Warehouse, Shop)
class AuthorAdmin(admin.ModelAdmin):
    pass


################
# Pocket Admin #
################
@admin.register(PocketFormat, PocketOrientation, PocketOption, PocketType)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Pocket)
class PocketInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse', 'type')


######################
# Price Holder Admin #
######################
@admin.register(PriceHolderFormat, PriceHolderHeight, PriceHolderType, PriceHolderWight)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceHolder)
class PriceHolderInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse', 'type')


#####################
# Price Paper Admin #
#####################
@admin.register(PricePaperFormat, PricePaperType)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PricePaper)
class PricePaperInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse', 'type')


########################
# Plastic Holder Admin #
########################
@admin.register(PlasticHolderOrientation, PlasticHolderPosition, PlasticHolderType, PlasticHolderFormat)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PlasticHolder)
class PlasticHolderInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse', 'type')


######################
# Price Holder Admin #
######################
@admin.register(OtherName, OtherType)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Other)
class OtherInstanceAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse', 'type')
