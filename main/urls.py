# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Mapea la ruta vacía (/) a la función home de views.py
    path('', views.home, name='home'), 
]