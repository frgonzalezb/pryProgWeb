# Aquí va lo del widget para el carrito:
from django import views
from django.urls import path
from .views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

app_name = "carrito"

# Aquí van las urls:
urlpatterns = [
    path("agregar/<int:producto_id>", agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>", eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>", restar_producto, name="restar"),
    path("limpiar/", limpiar_carrito, name="limpiar"),
]