from django.urls import path
from .views import VRegistro, user_login

urlpatterns = [
    path('registro/', VRegistro.as_view(), name="registro"),
    path('login/', user_login, name="login"),
]