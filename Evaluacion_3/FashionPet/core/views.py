# Librerías importadas aquí:
from django.http import Http404
from django.shortcuts import render, redirect
from core.models import Producto, Categoria
from .forms import CustomUserForm, ProductoForm

# Esto es para los productos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Esto de aquí abajo es para requerir usuario logueado y/o permisos para acceder a ciertas partes
# (se debe agregar @login_required o @permission_required() encima de los def correspondientes):
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate



# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def buscador(self, request):
    s=request.GET["s"]
    productos=Producto.objects.filter(nombre__icontains=s)
    data = {
        'productos':productos
    }
    return render(request, 'core/buscador.html', data)



class productos(ListView):
    model = Producto
    paginate_by = 4
    template_name = 'core/productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class detalle_producto(DetailView):
    model = Producto
    template_name = 'core/detalle_producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



'''
def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/productos.html', data)


def detalle_producto(request, id, slug):
    try:
        productos = Producto.objects.get(id=id, slug=slug)
    except:
        raise Http404('No se encuentra el producto especificado.')
    
    data = {
        'productos':productos,
    }
    return render(request, 'core/detalle_producto.html', data)
'''



# Aquí van las defs del CRUD para el gerente o el admin:
@login_required
def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/listado_productos.html', data)

@permission_required('core.add_producto')
def agregar_producto(request):
    data = {
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado correctamente'

    return render(request, 'core/agregar_producto.html', data)

@permission_required('core.change_producto')
def modificar_productos(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado correctamente'
            data['form'] = formulario

    return render(request, 'core/modificar_productos.html', data)

@permission_required('core.delete_producto')
def eliminar_productos(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="listado_productos")
