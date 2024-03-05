from django import views
from django.urls import path
from .views import inicio, contacto, quienes_somos, buscador, productos, detalle_producto, listado_productos, agregar_producto, modificar_productos, eliminar_productos

# Aquí van las urls:
urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio/', inicio, name="inicio"),
    path('contacto/', contacto, name="contacto"),
    path('quienes-somos/', quienes_somos, name="quienes_somos"),
    path('buscador/', buscador, name="buscador"),
    path('productos/', productos.as_view(), name="productos"),
    path('detalle-producto/<id>/<slug>/', detalle_producto.as_view(), name="detalle_producto"),
    path('listado-productos/', listado_productos, name="listado_productos"),
    path('agregar-producto', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_productos, name="modificar_productos"),
    path('eliminar-producto/<id>/', eliminar_productos, name="eliminar_productos"),
]