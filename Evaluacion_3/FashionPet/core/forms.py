# Importando librerías
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class ProductoForm(ModelForm):
    # Bloquecito de validación agregado posteriormente...
    nombre = forms.CharField(min_length=5, max_length=200)

    class Meta:
        model = Producto
        fields = ['nombre','tipoMascota','descripcion','categoria', 'precio', 'stock']
