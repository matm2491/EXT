from django.urls import path
from directorio.views import listado, crear, editar, ver, eliminar, BuscarView
from . import views



urlpatterns = [

    path('',views.index, name='index'),
    path('base', views.base, name='base'),
    path('leer', listado.as_view(template_name = "listado.html"), name='leer'),
    path('crear', crear.as_view(template_name = "crear.html"),name='crear'),
    path('editar/<int:pk>', editar.as_view(template_name = "editar.html"),name='editar'),
    path('ver/<int:pk>', ver.as_view(template_name = "ver.html"), name='ver'),  
    path('eliminar/<int:pk>', eliminar.as_view(), name='eliminar'),  
    path('buscar', BuscarView.as_view(), name='buscar')
]