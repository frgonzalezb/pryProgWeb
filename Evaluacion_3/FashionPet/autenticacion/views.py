from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class VRegistro(View):
    # Muestra el formulario:
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'autenticacion/registro.html', {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)

            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'autenticacion/registro.html', {"form":form})


def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            usuario=authenticate(username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, "ERROR: Este usuario no se encontra registrado.")
        
        else:
            messages.error(request, "ERROR: Los datos ingresados no son válidos.")

    form=AuthenticationForm()
    return render(request, 'autenticacion/login.html', {"form":form})
