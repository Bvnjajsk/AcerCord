from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import render
from django.core import serializers

# Create your views here.


def base (request):

    return render(request, 'app/base/base.html')


def home (request):

    return render(request, 'app/index/index.html')

def carrito (request):

    productos = Producto.objects.all()
    productos_json = serializers.serialize('json', productos)
    data ={
        'productos': productos_json

    }

    return render(request, 'app/carrito/carrito.html', data)
    

def categoria (request):
    return render(request, 'app/categoria/index.html')

def info_producto (request):
    return render(request, 'app/info_producto/index.html')

def login (request):
    return render(request, 'app/login/login.html')

def registrar (request):
    return render(request, 'app/registrar/index.html')

def pago (request):
    return render(request, 'app/pago/indexp.html')

def profile (request):
    return render(request, 'app/profile/profile.html')



@login_required
def contacto (request):
    data ={
        'form':ContactoForm()


    }
    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Enviado"

        else:
            data['form'] = formulario


    return render(request, 'app/contacto/index.html',data)

def catalogo (request):
    productos = Producto.objects.all()
    data ={
        'productos': productos


    }
    return render(request, 'app/catalogo/indexc.html',data)

def pago (request):
    return render(request, 'app/pago/indexp.html')



@permission_required('app.add_producto')
def agregar_producto(request):


    data ={
''      'form':ProductoForm()

    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Registrado")

        else:
            data["form"]= formulario

    return render (request,'app/agregarp/agregar.html',data)



def listar_producto (request):
    lproductos = Producto.objects.all()
    data ={
        'productos':lproductos
        
    }



    return render(request, 'app/agregarp/listar.html',data)




@permission_required('app.change_producto')
def modificar_producto (request,id):

        mproducto = get_object_or_404(Producto, codigo=id)

        data = {
            'form': ProductoForm(instance=mproducto)

        }

        if request.method =='POST':
            formulario = ProductoForm(data=request.POST, instance=mproducto, files =request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request,"Modificado Correctamente")
                return redirect(to="listar_producto")
            data['form'] = formulario


        return render(request, 'app/agregarp/modificar.html',data)


@permission_required('app.delete_producto')
def eliminar_producto(request,id):
    eproducto = get_object_or_404(Producto, codigo=id)
    eproducto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="listar_producto")




def registro (request):
    data={
        'form': CustomUserCreationForm()

    }




    if request.method =='POST':
        rformulario = CustomUserCreationForm(data =request.POST)
        if rformulario.is_valid():
            rformulario.save()

            messages.success(request, "Te has registrado Correctamente")
            return redirect(to="login")
        data['form'] = rformulario


    return render(request, 'registration/registro.html',data)


def buscar (request):
    query = request.GET.get('pbuscar')

    if query:
        bproductos = Producto.objects.filter(nombre__icontains=query)

    else:
        bproductos = Producto.objects.all()

    data ={
        'productos':bproductos
        
    }

    return render(request, 'app/buscar/busca.html',data)