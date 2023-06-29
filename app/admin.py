from django.contrib import admin
from .models import Usuario, Fierros,Producto,Contacto


class ProductoAdmin(admin.ModelAdmin):
    list_display  =  ["codigo","nombre","precio"]  
    list_editable =  ["precio"]                     
    search_fields =  ["nombre"]                     
    list_filter   =  ["precio"]                     



admin.site.register(Usuario)
admin.site.register(Fierros)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contacto)
