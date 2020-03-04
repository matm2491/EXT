from django.urls import path
from . import views

urlpatterns = [

    path('direccion', views.direccion, name='direccion')
]