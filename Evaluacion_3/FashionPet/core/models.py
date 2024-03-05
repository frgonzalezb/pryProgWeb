from django.db import models
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = AutoSlugField(unique_with="id", populate_from='nombre')
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class TipoMascota(models.Model):
    nombre = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='id', editable=True)
    tipoMascota= models.ForeignKey(TipoMascota, on_delete=CASCADE)
    descripcion = models.CharField(max_length=1000)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    precio = models.IntegerField()
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
