from django.contrib import admin

from .models import TinUsuarios, TinDependencias




class FuncionariosAdmin(admin.ModelAdmin):

    
    list_display=("primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido")
    search_fields=("primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido")






admin.site.register(TinUsuarios, FuncionariosAdmin)

admin.site.register(TinDependencias)