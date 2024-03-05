from django.shortcuts import render, redirect
from core.models import Producto
from .carrito import Carrito

# Create your views here.

# Acción para añadir productos al carrito:
def agregar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect(to='productos')
    
# Acción para eliminar productos al carrito:
def eliminar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect(to='productos')

# Acción para restar productos al carrito:
def restar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect(to='productos')

# Acción para limpiar carrito:
def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar_carrito()
    return redirect(to='productos')
