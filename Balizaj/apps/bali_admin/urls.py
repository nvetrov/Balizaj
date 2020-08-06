from django.urls import path
from . import views

urlpatterns = [
    path('reports', views.reports),
    path('move_between_storage', views.move_between_storage),
]
