# main/urls.py

from django.urls import path
from . import views # Asegúrate que esto sea correcto

urlpatterns = [
    path('', views.home, name='home'), # Verifica que views.home exista y no tenga errores
]