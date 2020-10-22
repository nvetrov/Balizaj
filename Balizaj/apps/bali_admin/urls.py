from django.urls import path
from . import views

urlpatterns = [
    path('reports', views.reports),
    path('select_move_storage', views.select_move_storage),
    path('move_materials', views.move_materials, name='move_materials')
]
