from django.contrib import admin
from .models import *


# Register your models here.
################
# Pocket Admin #
################

@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Format)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PocketOption)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Orientation)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PocketType)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Pocket)
class PocketInstanseAdmin(admin.ModelAdmin):
    list_filter = ('shop', 'warehouse')