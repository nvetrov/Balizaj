from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pockets', views.pockets_type),
    path('priceholders', views.priceholders_type),
    path('plasticholders', views.plasticholders_type),
    path('pricepaper', views.pricepaper_type),
    path('other', views.other_type),
    path('<name>/<int:type_id>/', views.materials),
    path('cart', views.cart),
    path('write_off', views.write_off)
]
