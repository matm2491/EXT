from django.shortcuts import render

from django.urls import reverse

from django.template import loader

from django.http import HttpResponse
#importamos los modelos
from .models import TinUsuarios, TinDependencias

#importamos los formularios
from django import forms


from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 


 #para el buscador
from django.views.generic import TemplateView



#primera vista de prueba
def index(request):

    

    return render(request, 'index.html', {})



#vistas para el directorio

def base(request):

    return render(request, 'base.html')



class listado(ListView):
    model = TinDependencias
    model = TinUsuarios
   
    

class crear(SuccessMessageMixin, CreateView):
    model = TinUsuarios
    form = TinUsuarios
    fields = "__all__"
    success_message = "¡Agregado exitosamente!"

    def get_success_url(self):
        return reverse('leer')

class ver(DetailView):
    model = TinUsuarios


class editar(UpdateView):
    model = TinUsuarios
    form = TinUsuarios
    fields = "__all__"
    
    def get_success_url(self):
        return reverse('leer')

class eliminar(DeleteView):
    model = TinUsuarios
    form = TinUsuarios
    fields = "__all__"

    def get_success_url(self):
        success_message = '¡Funcionario eliminado correctamente!' 
        messages.success (self.request, (success_message))       
        return reverse('leer')


class BuscarView(TemplateView):
    

    pass
       