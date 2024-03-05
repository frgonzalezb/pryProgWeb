from django.contrib import admin
from .models import Categoria, Producto, TipoMascota

# Register your models here.

admin.site.register(Categoria)
admin.site.register(TipoMascota)
admin.site.register(Producto)