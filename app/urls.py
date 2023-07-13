from django.urls import path
from .views import *



urlpatterns = [
    path('base', base, name="base"),
    path('', home, name="home"),
    path('carrito/',carrito, name ="carrito" ),
    path('catalogo/',catalogo, name ="catalogo" ),
    path('categoria/',categoria, name ="categoria" ),
    path('info_producto/',info_producto, name ="info_producto" ),
    path('login/',login, name ="login" ),
    path('pago/',pago, name ="pago" ),
    path('registrar/',registrar, name ="registrar" ),
    path('contacto/',contacto, name ="contacto" ),
    path('profile/',profile, name ="profile" ),
    path('agregar-producto/',agregar_producto, name ="agregar_producto" ),
    path('listar-producto/',listar_producto, name ="listar_producto" ),
    path('buscar/',buscar, name="buscar"),
    path('modificar-producto/<id>/',modificar_producto, name ="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto, name ="eliminar_producto"),

    path('registro/',registro, name="registro"),
    
]
